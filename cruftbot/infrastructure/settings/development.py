"""Framework settings for local development."""
from cruftbot.infrastructure.settings.components.cross_origin_resource_sharing import (
    CORS_ALLOWED_ORIGINS,
)
from cruftbot.infrastructure.settings.components.debug_toolbar import *
from cruftbot.infrastructure.settings.components.extensions import *
from cruftbot.infrastructure.settings.components.migration_linter import *
from cruftbot.infrastructure.settings.components.querycount import *
from cruftbot.infrastructure.settings.components.test_migrations import *
from cruftbot.infrastructure.settings.production import *


DEBUG = True

ROOT_URLCONF = "cruftbot.infrastructure.urls.development"

DEVELOPMENT_ORIGINS = ["http://localhost:8000", "http://0.0.0.0:8000"]

CORS_ALLOWED_ORIGINS.extend(DEVELOPMENT_ORIGINS)
