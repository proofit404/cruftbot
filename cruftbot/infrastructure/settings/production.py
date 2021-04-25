"""Framework settings for production environment."""
from cruftbot.infrastructure.settings.components.activity_stream import *
from cruftbot.infrastructure.settings.components.axes import *
from cruftbot.infrastructure.settings.components.base import *
from cruftbot.infrastructure.settings.components.content_security_policy import *
from cruftbot.infrastructure.settings.components.filters import *
from cruftbot.infrastructure.settings.components.node_assets import *
from cruftbot.infrastructure.settings.components.permissions_policy import *
from cruftbot.infrastructure.settings.components.staticfiles import *
from cruftbot.infrastructure.settings.components.templates import *


DEBUG = False

ROOT_URLCONF = "cruftbot.infrastructure.urls.production"
