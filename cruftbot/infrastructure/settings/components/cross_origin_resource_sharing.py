"""Settings for CORS headers application."""
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


INSTALLED_APPS.append("corsheaders")

MIDDLEWARE.append("corsheaders.middleware.CorsMiddleware")

CORS_ALLOWED_ORIGINS = ["https://cruftbot.io"]
