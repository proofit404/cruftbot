"""HTTP request routing for local development."""
import debug_toolbar
from django.contrib.staticfiles.views import serve
from django.urls import include
from django.urls import path
from django.urls import re_path

from cruftbot.infrastructure.urls import urlpatterns


development_patterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    re_path(r"^static/(?P<path>.*)$", serve),
]

urlpatterns.extend(development_patterns)
# @todo #251 Define own patterns variable. Include production urls
#  in it without import. We need to address a very similar problem
#  for settings files in #230 task. Production routing should be
#  defined in the dedicated module. Move it from package dunder
#  init module.
