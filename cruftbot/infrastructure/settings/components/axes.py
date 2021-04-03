from cruftbot.infrastructure.settings.components.base import AUTHENTICATION_BACKENDS
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


INSTALLED_APPS.append("axes")

# Axes should be the first backend in the list.
AUTHENTICATION_BACKENDS.insert(0, "axes.backends.AxesBackend")

# Axes should be the last middleware in the list.
MIDDLEWARE.append("axes.middleware.AxesMiddleware")
