from debug_toolbar.settings import PANELS_DEFAULTS

from cruftbot.settings import *


DEVELOPMENT_APPS = ["django_extensions", "debug_toolbar", "stories_django"]

INSTALLED_APPS.extend(DEVELOPMENT_APPS)

DEVELOPMENT_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "querycount.middleware.QueryCountMiddleware",
]

MIDDLEWARE.extend(DEVELOPMENT_MIDDLEWARE)

ROOT_URLCONF = "cruftbot.urls.development"

INTERNAL_IPS = ["127.0.0.1"]

DEVELOPMENT_PANELS = ["stories_django.debug_toolbar.StoriesPanel"]

DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + DEVELOPMENT_PANELS
