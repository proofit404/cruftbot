"""Settings for SecurityMiddleware class."""
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


MIDDLEWARE.insert(0, "django.middleware.security.SecurityMiddleware")

SECURE_REFERRER_POLICY = "no-referrer"

SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = True
