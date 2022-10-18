from i18n import add_translation as _

from raid.parsing import AlertStatus, Threat

__locale__ = "en"

_(
    f"{Threat.AirRaid}.{AlertStatus.Active}",
    "%{status}%{threat} %{time} Air raid alert in %{location}.%{mentions}",
    __locale__,
)
_(
    f"{Threat.AirRaid}.{AlertStatus.Inactive}",
    "%{status}%{threat} %{time} Air raid alert in %{location} cancelled.%{mentions}",
    __locale__,
)

_(
    f"{Threat.ArtilleryShelling}.{AlertStatus.Active}",
    "%{status}%{threat} %{time} Artillery shelling in %{location}.%{mentions}",
    __locale__,
)
_(
    f"{Threat.ArtilleryShelling}.{AlertStatus.Inactive}",
    (
        "%{status}%{threat} %{time} Artillery shelling in %{location} cancelled.",
        "%{mentions}",
    ),
    __locale__,
)
