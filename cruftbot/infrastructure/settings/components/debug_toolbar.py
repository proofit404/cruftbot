"""Settings for debug toolbar application."""
from debug_toolbar.settings import PANELS_DEFAULTS

from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE
from cruftbot.infrastructure.settings.components.templates import TEMPLATES


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


TEMPLATES.append(
    {"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": True}
)
# @todo #205 Remove debug toolbar templates workaround. After we
#  fix template render in the toolbar application upstream, we
#  should remove Django templates engine from list.
