"""Settings for session contrib application."""
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


INSTALLED_APPS.append("django.contrib.sessions")

MIDDLEWARE.insert(0, "django.contrib.sessions.middleware.SessionMiddleware")

SESSION_COOKIE_SECURE = True
