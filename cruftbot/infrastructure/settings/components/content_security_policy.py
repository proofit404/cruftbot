"""Settings for content security policy application."""
from cruftbot.infrastructure.settings.components.base import MIDDLEWARE


MIDDLEWARE.append("csp.middleware.CSPMiddleware")

CSP_STYLE_SRC = ("'self'",)

CSP_SCRIPT_SRC = ("'self'",)

CSP_FONT_SRC = ("'self'",)

CSP_IMG_SRC = ("'self'", "data:")

CSP_DEFAULT_SRC = ("'none'",)

# @todo #15 Configure CSP Violation Reports
#  (https://django-csp.readthedocs.io/en/latest/reports.html).
#  Debug toolbar does not work with too strict settings.
