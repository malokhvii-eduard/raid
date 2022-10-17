import asyncio
from enum import Enum
from functools import lru_cache

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


async def format_alert(alert: Alert, locale: Locale) -> str:
    _set_i18n_option("locale", locale)

    fields = {
        "status": alert["status"],
        "time": alert["time"].strftime(_ALERT_TIME_FORMAT),
        "threat": alert["threat"],
        "location": await _translate_alert_location(alert["location"], locale),
    }

    return translate(f"{alert['threat']}.{alert['status']}", **fields)


async def _translate_alert_location(location: str, locale: Locale) -> str:
    if locale == _ALERT_LOCATION_SOURCE_LOCALE:
        return location

    loop = asyncio.get_event_loop()
    translator = _get_alert_location_translator(locale)
    return await loop.run_in_executor(None, translator.translate, location)


@lru_cache(maxsize=None)
def _get_alert_location_translator(target_locale: Locale) -> GoogleTranslator:
    return GoogleTranslator(_ALERT_LOCATION_SOURCE_LOCALE, target_locale)
