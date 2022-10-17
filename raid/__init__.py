import sys
from copy import copy
from functools import partial
from typing import Any, Dict

import typer
from loguru import logger
from slack_sdk.http_retry.builtin_async_handlers import (
    AsyncConnectionErrorRetryHandler,
    AsyncRateLimitErrorRetryHandler,
)
from slack_sdk.webhook.async_client import AsyncWebhookClient
from telethon import TelegramClient, events
from telethon.tl.custom.message import Message

from raid.formatter import Locale, format_alert, load_translations
from raid.parsing import ParseError, parse_alert

_LOGGER_FORMAT = (
    "<g>{time:YYYY-MM-DD HH:mm:ss.SSS}</g> | <lvl>{level: <8}</lvl>"
    " | <lvl>{message}</lvl> | {extra}"
)

__version__ = "1.0.0"

app = typer.Typer()


async def notify_of_alert(
    event: Message, webhook_client: AsyncWebhookClient, locale: Locale
) -> None:
    event_logger = logger.bind(event_id=event.id)
    event_logger.debug("event.received", raw_text=event.raw_text)

    try:
        alert = parse_alert(event.raw_text, event.date)
        event_logger.debug("event.parsed", alert=alert)
    except ParseError:
        event_logger.exception("event.not_parsed", raw_text=event.raw_text)
        return

    message = await format_alert(alert, locale)
    event_logger.debug("alert.formatted", message=message, locale=locale.value)

    try:
        response = await webhook_client.send(text=message)
        if response.status_code == 200:
            event_logger.info("alert.sent", message=message)
        else:
            event_logger.error(
                "alert.not_sent", message=message, status_code=response.status_code
            )
    except (Exception,):
        event_logger.exception("alert.not_sent", message=message)


def print_version(value: bool) -> None:
    if value:
        print(f"raid: {__version__}")
        raise typer.Exit()


@app.command()
def main(
    api_id: int = typer.Argument(..., envvar="RAID_API_ID", help="Telegram API id."),
    api_hash: str = typer.Argument(
        ..., envvar="RAID_API_HASH", help="Telegram API hash."
    ),
    webhook_url: str = typer.Argument(
        ..., envvar="RAID_WEBHOOK_URL", help="Slack incoming webhook."
    ),
    chat_id: int = typer.Option(
        default=1766138888,
        help=(
            "Source of alerts. By default, the tool monitors alerts from the"
            " official channel https://t.me/air_alert_ua."
        ),
    ),
    max_retries: int = typer.Option(
        default=3,
        help="The maximum amount of retries attempts for sending messages to Slack.",
    ),
    locale: Locale = typer.Option(
        Locale.uk.value, help="The language of outgoing messages about alerts."
    ),
    verbose: bool = typer.Option(
        False, "-v", "--verbose", help="Show information about alerts."
    ),
    version: bool = typer.Option(
        False,
        "-V",
        "--version",
        callback=print_version,
        is_eager=True,
        help="Show version and exit.",
    ),
    debug: bool = typer.Option(
        False,
        "--debug",
        help="Show information useful for debugging and for reporting bugs.",
    ),
) -> None:
    """
    A simple tool to get immediate notifications in Slack once your Ukrainian
    colleagues become unavailable due to an air raid or artillery shelling
    threats.
    """
    logger.remove()

    if verbose:
        logger_common = {"format": _LOGGER_FORMAT, "enqueue": True}

        logger.configure(patcher=_patch_record)
        logger.add(
            sys.stdout,
            level="DEBUG" if debug else "INFO",
            filter=lambda r: r["level"].no < 40,
            **logger_common,
        )
        logger.add(sys.stderr, level="ERROR", **logger_common)

    webhook_client = AsyncWebhookClient(
        webhook_url,
        retry_handlers=[
            AsyncConnectionErrorRetryHandler(max_retry_count=max_retries),
            AsyncRateLimitErrorRetryHandler(max_retry_count=max_retries),
        ],
    )

    load_translations(locale)

    client = TelegramClient("raid", api_id, api_hash, auto_reconnect=True)
    with client:
        logger.info("client.connected", api_id=api_id, chat_id=chat_id)

        client.add_event_handler(
            partial(notify_of_alert, webhook_client=webhook_client, locale=locale),
            events.NewMessage(chats=[chat_id]),
        )
        client.run_until_disconnected()


def _patch_record(record: Dict[str, Any]) -> None:
    if "alert" in record["extra"]:
        alert = copy(record["extra"]["alert"])
        alert["status"] = str(alert["status"])
        alert["time"] = alert["time"].isoformat()
        alert["threat"] = str(alert["threat"])
        record["extra"]["alert"] = alert


if __name__ == "main":
    app()
