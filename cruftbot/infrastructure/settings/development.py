"""Framework settings for local development."""
from cruftbot.infrastructure.settings.components.activity_stream import *
from cruftbot.infrastructure.settings.components.axes import *
from cruftbot.infrastructure.settings.components.base import *
from cruftbot.infrastructure.settings.components.base import CORS_ALLOWED_ORIGINS
from cruftbot.infrastructure.settings.components.content_security_policy import *
from cruftbot.infrastructure.settings.components.debug_toolbar import *
from cruftbot.infrastructure.settings.components.extensions import *
from cruftbot.infrastructure.settings.components.extra_checks import *
from cruftbot.infrastructure.settings.components.filters import *
from cruftbot.infrastructure.settings.components.guardian import *
from cruftbot.infrastructure.settings.components.migration_linter import *
from cruftbot.infrastructure.settings.components.node_assets import *
from cruftbot.infrastructure.settings.components.permissions_policy import *
from cruftbot.infrastructure.settings.components.querycount import *
from cruftbot.infrastructure.settings.components.staticfiles import *
from cruftbot.infrastructure.settings.components.templates import *
from cruftbot.infrastructure.settings.components.test_migrations import *


# @todo #183 Reuse components definition from the production file.
#  Development settings is simply an extension of used components
#  in addition to the production list. It would be nice not to
#  repeat components above this comment.


DEBUG = True

ROOT_URLCONF = "cruftbot.infrastructure.urls.development"

DEVELOPMENT_ORIGINS = ["http://localhost:8000", "http://0.0.0.0:8000"]

CORS_ALLOWED_ORIGINS.extend(DEVELOPMENT_ORIGINS)
