"""Settings for guardian application."""
from cruftbot.infrastructure.settings.components.base import AUTHENTICATION_BACKENDS
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS


INSTALLED_APPS.append("guardian")

AUTHENTICATION_BACKENDS.append("guardian.backends.ObjectPermissionBackend")
