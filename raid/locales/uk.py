from i18n import add_translation as _

from raid.parsing import AlertStatus, Threat

__locale__ = "uk"

_(
    f"{Threat.AirRaid}.{AlertStatus.Active}",
    "%{status}%{threat} %{time} Повітряна тривога в %{location}.",
    __locale__,
)
_(
    f"{Threat.AirRaid}.{AlertStatus.Inactive}",
    "%{status}%{threat} %{time} Повітряна тривога в %{location}.",
    __locale__,
)

_(
    f"{Threat.ArtilleryShelling}.{AlertStatus.Active}",
    "%{status}%{threat} %{time} Загроза артобстрілу в %{location}.",
    __locale__,
)
_(
    f"{Threat.ArtilleryShelling}.{AlertStatus.Inactive}",
    "%{status}%{threat} %{time} Відбій загрози артобстрілу в %{location}.",
    __locale__,
)
