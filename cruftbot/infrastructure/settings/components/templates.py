"""Settings for templates application."""
from django.templatetags.static import static
from django.urls import reverse
from jinja2.sandbox import SandboxedEnvironment


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": (
                "cruftbot.infrastructure.settings.components.templates.environment"
            )
        },
    },
]


def environment(**options):
    """Create safe Jinja environment."""
    env = SandboxedEnvironment(**options)
    scope = {"static": static, "url": reverse}
    env.globals.update(scope)
    return env
