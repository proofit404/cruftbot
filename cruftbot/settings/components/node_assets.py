from cruftbot.settings.components.base import BASE_DIR
from cruftbot.settings.components.base import INSTALLED_APPS
from cruftbot.settings.components.staticfiles import STATICFILES_FINDERS

# @todo #183 Components can not import each other. Split settings `include`
#  function execute python files instead of import. Thats means that if a
#  component were imported by another component and `include` function was
#  applied to it as well - it will be executed multiple times. And if this
#  component file do INSTALLED_APPS.append('app') it will be doubled.


INSTALLED_APPS.append("django_node_assets")

STATICFILES_FINDERS.append("django_node_assets.finders.NodeModulesFinder")

NODE_PACKAGE_JSON = BASE_DIR / "package.json"

NODE_MODULES_ROOT = BASE_DIR / "node_modules"
