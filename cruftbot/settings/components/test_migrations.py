from cruftbot.settings.components.base import INSTALLED_APPS


INSTALLED_APPS.append("django_test_migrations.contrib.django_checks.AutoNames")

DTM_IGNORED_MIGRATIONS = {("axes", "*")}
