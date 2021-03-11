from pathlib import Path

from environ import Env


env = Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env.str("CRUFTBOT_SECRET_KEY")

DEBUG = env.bool("CRUFTBOT_DEBUG")

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "actstream",
    "axes",
    "rest_framework",
    "drf_yasg",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.gitlab",
    "corsheaders",
    "cruftbot.apps.CruftbotConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "csp.middleware.CSPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"environment": "jinja2.sandbox.SandboxedEnvironment"},
    },
]

ROOT_URLCONF = "cruftbot.urls.production"

WSGI_APPLICATION = "cruftbot.wsgi.application"

SITE_ID = env.int("CRUFTBOT_SITE_ID")

DATABASES = {"default": env.db("CRUFTBOT_DATABASE_URL")}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        )
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_PROVIDERS = {}

CORS_ALLOWED_ORIGINS = ["https://cruftbot.io"]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"

CSP_STYLE_SRC = ("'self'", "cdn.jsdelivr.net")

CSP_SCRIPT_SRC = ("'self'", "cdn.jsdelivr.net")

CSP_FONT_SRC = ("'self'",)

CSP_IMG_SRC = ("'self'", "data:")

CSP_DEFAULT_SRC = ("'none'",)

# @todo #15 Configure CSP Violation Reports
#  (https://django-csp.readthedocs.io/en/latest/reports.html).
#  Debug toolbar does not work with too strict settings.

# @todo #171 Split common settings into separate components.
