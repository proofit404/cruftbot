"""Settings for health check application."""
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS


INSTALLED_APPS.extend(
    [
        "health_check",
        "health_check.db",
        "health_check.cache",
        "health_check.storage",
        "health_check.contrib.migrations",
    ]
)
