"""Settings for permissions policy application."""
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


MIDDLEWARE.append("django_permissions_policy.PermissionsPolicyMiddleware")

PERMISSIONS_POLICY = {"autoplay": [], "geolocation": []}
