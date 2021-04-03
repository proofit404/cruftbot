from split_settings.tools import include

from cruftbot.infrastructure.settings.components.base import CORS_ALLOWED_ORIGINS


include(
    "components/base.py",
    "components/templates.py",
    "components/staticfiles.py",
    "components/node_assets.py",
    "components/activity_stream.py",
    "components/content_security_policy.py",
    "components/axes.py",
    # @todo #183 Reuse components definition from the production file.
    #  Development settings is simply an extension of used components
    #  in addition to the production list. It would be nice not to
    #  repeat components above this comment.
    "components/debug_toolbar.py",
    "components/extensions.py",
    "components/querycount.py",
    "components/extra_checks.py",
    "components/migration_linter.py",
    "components/test_migrations.py",
)

DEBUG = True

ROOT_URLCONF = "cruftbot.infrastructure.urls.development"

DEVELOPMENT_ORIGINS = ["http://localhost:8000", "http://0.0.0.0:8000"]

CORS_ALLOWED_ORIGINS.extend(DEVELOPMENT_ORIGINS)
