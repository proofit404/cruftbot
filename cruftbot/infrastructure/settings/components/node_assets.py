"""Settings for node assets application."""
from cruftbot.infrastructure.settings.components.base import BASE_DIR
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS
from cruftbot.infrastructure.settings.components.staticfiles import STATICFILES_FINDERS


INSTALLED_APPS.append("django_node_assets")

STATICFILES_FINDERS.append("django_node_assets.finders.NodeModulesFinder")

NODE_PACKAGE_JSON = BASE_DIR / "package.json"

NODE_MODULES_ROOT = BASE_DIR / "node_modules"
