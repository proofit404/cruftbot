from cruftbot.settings.components.base import INSTALLED_APPS


INSTALLED_APPS.append("django.contrib.staticfiles")

STATIC_URL = "/static/"

STATICFILES_FINDERS = ["django.contrib.staticfiles.finders.AppDirectoriesFinder"]

# @todo #89 Staticfiles contrib application does not work. Every request result
#  in 404 NOT FOUND error. There is debug toolbar warning on server startup. It
#  requires STATICFILES_DIRS to exists.
