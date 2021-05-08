"""Database settings."""
from cruftbot.infrastructure.settings.components.base import env

DATABASES = {"default": env.db("CRUFTBOT_DATABASE_URL")}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
