import re
from datetime import datetime
from enum import Enum
from typing import TypedDict

import pytz

_ALERT_TIME_ZONE = pytz.timezone("Europe/Kiev")
_ALERT_PATTERN = re.compile(
    (
        r"^(?P<status>.)"
        r".*(?:тривог[аи] в|Зараз у|артобстрілу в)\s"
        r"(?P<location>.*)"
        r"\s(?:Слідкуйте|Зверніть|артилерійський).*"
        r"(?P<hashtag>#.*)$"
    ),
    re.DOTALL,
)
_ALERT_THREAT_PATTERN = re.compile(r"^.*(?P<threat>тривог|артобстріл).*$", re.DOTALL)
_ALERT_LOCATION_UNNECESSARY = re.compile(r"(м\.|\.)", re.DOTALL)


class ParseError(Exception):
    pass


class Threat(str, Enum):
    AirRaid = "🚀"
    ArtilleryShelling = "💣"

    def __str__(self) -> str:
        return self.value  # noqa


class AlertStatus(str, Enum):
    Active = "🔴"
    Inactive = "🟢"

    def __str__(self) -> str:
        return self.value  # noqa


class Alert(TypedDict):
    status: AlertStatus
    time: datetime
    threat: Threat
    location: str
    hashtag: str


def parse_alert(text: str, time: datetime) -> Alert:
    match = _ALERT_PATTERN.match(text)
    if not match:
        raise ParseError("The text doesn't match the alert pattern.")

    return {
        "status": _parse_alert_status(match["status"]),
        "time": _normalize_alert_time(time),
        "threat": _parse_alert_threat(text),
        "location": _normalize_alert_location(match["location"]),
        "hashtag": match["hashtag"],
    }


def _parse_alert_threat(text: str) -> Threat:
    match = _ALERT_THREAT_PATTERN.match(text)
    if not match:
        raise ParseError("The text doesn't match the threat pattern.")

    threat = match["threat"]
    if threat == "тривог":
        return Threat.AirRaid
    else:
        return Threat.ArtilleryShelling


def _parse_alert_status(status: str) -> AlertStatus:
    return AlertStatus.Active if status == AlertStatus.Active else AlertStatus.Inactive


def _normalize_alert_time(time: datetime) -> datetime:
    return time.astimezone(_ALERT_TIME_ZONE)


def _normalize_alert_location(location: str) -> str:
    return _ALERT_LOCATION_UNNECESSARY.sub("", location).strip()
