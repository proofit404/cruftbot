"""Settings for SecurityMiddleware class."""
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


MIDDLEWARE.insert(0, "django.middleware.security.SecurityMiddleware")

SECURE_REFERRER_POLICY = "no-referrer"
