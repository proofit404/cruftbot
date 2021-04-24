"""Settings for staticfiles application."""
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS


INSTALLED_APPS.append("django.contrib.staticfiles")

STATIC_URL = "/static/"

STATICFILES_FINDERS = ["django.contrib.staticfiles.finders.AppDirectoriesFinder"]
