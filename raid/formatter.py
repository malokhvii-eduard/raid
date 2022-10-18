import asyncio
from datetime import datetime
from enum import Enum
from functools import lru_cache
from typing import Iterable

from deep_translator import GoogleTranslator
from i18n import set as _set_i18n_option
from i18n import t as translate

from raid.parsing import Alert


class Locale(str, Enum):
    en = "en"
    uk = "uk"


_ALERT_TIME_FORMAT = "%H:%M"
_ALERT_LOCATION_SOURCE_LOCALE = Locale.uk


def load_translations(locale: Locale) -> None:
    __import__(f"raid.locales.{locale}")


async def format_alert(alert: Alert, member_ids: Iterable[str], locale: Locale) -> str:
    _set_i18n_option("locale", locale)

    fields = {
        "status": alert["status"],
        "time": _format_alert_time(alert["time"]),
        "threat": alert["threat"],
        "location": await _translate_alert_location(alert["location"], locale),
        "mentions": f" {_format_mentions(member_ids)}" if member_ids else "",
    }

    return translate(f"{alert['threat']}.{alert['status']}", **fields)


def _format_alert_time(time: datetime) -> str:
    return time.strftime(_ALERT_TIME_FORMAT)


def _format_mentions(member_ids: Iterable[str]) -> str:
    return ", ".join(map(lambda x: f"<@{x}>", set(member_ids))) if member_ids else ""


async def _translate_alert_location(location: str, locale: Locale) -> str:
    if locale == _ALERT_LOCATION_SOURCE_LOCALE:
        return location

    loop = asyncio.get_event_loop()
    translator = _get_alert_location_translator(locale)
    return await loop.run_in_executor(None, translator.translate, location)


@lru_cache(maxsize=None)
def _get_alert_location_translator(target_locale: Locale) -> GoogleTranslator:
    return GoogleTranslator(_ALERT_LOCATION_SOURCE_LOCALE, target_locale)
