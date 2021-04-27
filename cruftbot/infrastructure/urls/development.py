"""HTTP request routing for local development."""
from django.contrib.staticfiles.views import serve
from django.urls import include
from django.urls import path
from django.urls import re_path


urlpatterns = [
    path("", include("cruftbot.infrastructure.urls.production")),
    path("__debug__/", include("debug_toolbar.toolbar")),
    re_path(r"^static/(?P<path>.*)$", serve),
]
