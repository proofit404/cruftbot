from split_settings.tools import include


include(
    "components/base.py",
    "components/templates.py",
    "components/staticfiles.py",
    "components/node_assets.py",
)

DEBUG = False

ROOT_URLCONF = "cruftbot.urls.production"
