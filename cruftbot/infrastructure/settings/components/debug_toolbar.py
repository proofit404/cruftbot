"""Settings for debug toolbar application."""
from debug_toolbar.settings import PANELS_DEFAULTS

from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


INSTALLED_APPS.append("debug_toolbar")

INSTALLED_APPS.append("stories_django")

MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + ["stories_django.debug_toolbar.StoriesPanel"]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "cruftbot.infrastructure.settings.development.show_toolbar"
}


def show_toolbar(request):
    """Show debug toolbar no matter docker."""
    return True


# @todo #190 Debug toolbar does not work without django template engine enabled.
#  We have Jinja2 engine enabled only.
