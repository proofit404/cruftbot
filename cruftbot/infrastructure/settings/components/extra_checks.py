"""Settings for extra checks application."""
from cruftbot.infrastructure.settings.components.base import INSTALLED_APPS


INSTALLED_APPS.append("extra_checks")

EXTRA_CHECKS = {
    "checks": [
        "no-unique-together",
        "no-index-together",
        "field-file-upload-to",
        "field-text-null",
        "field-boolean-null",
        "field-null",
        {"id": "field-foreign-key-db-index", "when": "indexes"},
        "field-default-null",
        "field-choices-constraint",
    ]
}
