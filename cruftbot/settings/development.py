from split_settings.tools import include

from cruftbot.settings.components.base import CORS_ALLOWED_ORIGINS
from cruftbot.settings.components.base import INSTALLED_APPS


include(
    "components/base.py",
    "components/templates.py",
    "components/staticfiles.py",
    "components/node_assets.py",
    "components/activity_stream.py"
    # @todo #183 Reuse components definition from the production file.
    #  Development settings is simply an extension of used components
    #  in addition to the production list. It would be nice not to
    #  repeat components above this comment.
    "components/debug_toolbar.py",
    "components/extensions.py",
    "components/querycount.py",
    "components/extra_checks.py",
)

DEBUG = True

ROOT_URLCONF = "cruftbot.urls.development"


DEVELOPMENT_APPS = [
    "django_test_migrations.contrib.django_checks.AutoNames",
    "django_migration_linter",
]

INSTALLED_APPS.extend(DEVELOPMENT_APPS)

DTM_IGNORED_MIGRATIONS = {("axes", "*")}

DEVELOPMENT_ORIGINS = ["http://localhost:8000", "http://0.0.0.0:8000"]

CORS_ALLOWED_ORIGINS.extend(DEVELOPMENT_ORIGINS)
