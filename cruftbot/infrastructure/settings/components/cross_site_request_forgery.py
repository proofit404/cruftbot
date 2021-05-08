"""Settings for Cross-Site Request Forgery."""
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


MIDDLEWARE.append("django.middleware.csrf.CsrfViewMiddleware")

CSRF_COOKIE_SECURE = True
