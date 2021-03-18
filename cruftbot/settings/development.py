from debug_toolbar.settings import PANELS_DEFAULTS
from split_settings.tools import include

from cruftbot.settings.components.base import CORS_ALLOWED_ORIGINS
from cruftbot.settings.components.base import INSTALLED_APPS
from cruftbot.settings.components.base import MIDDLEWARE


include(
    "components/base.py",
    "components/templates.py",
    "components/staticfiles.py",
    "components/node_assets.py",
)


def show_toolbar(request):
    return True


DEVELOPMENT_APPS = [
    "django_extensions",
    "debug_toolbar",
    "stories_django",
    "django_test_migrations.contrib.django_checks.AutoNames",
    "django_migration_linter",
    "extra_checks",
]

INSTALLED_APPS.extend(DEVELOPMENT_APPS)

DEVELOPMENT_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "querycount.middleware.QueryCountMiddleware",
]

MIDDLEWARE.extend(DEVELOPMENT_MIDDLEWARE)

ROOT_URLCONF = "cruftbot.urls.development"

DEVELOPMENT_PANELS = ["stories_django.debug_toolbar.StoriesPanel"]

DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + DEVELOPMENT_PANELS

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": "cruftbot.settings.development.show_toolbar"
}

SHELL_PLUS = "ipython"

SHELL_PLUS_PRINT_SQL = True

EXTRA_CHECKS = {
    "checks": [
        "no-unique-together",
        "no-index-together",
        "field-file-upload-to",
        "field-text-null",
        "field-boolean-null",
        "field-null",
        {"id": "field-foreign-key-db-index", "when": "indexes"},
        "field-default-null",
        "field-choices-constraint",
    ]
}

DTM_IGNORED_MIGRATIONS = {("axes", "*")}

DEVELOPMENT_ORIGINS = ["http://localhost:8000", "http://0.0.0.0:8000"]

CORS_ALLOWED_ORIGINS.extend(DEVELOPMENT_ORIGINS)
