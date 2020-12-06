import debug_toolbar
from django.urls import include
from django.urls import path

from cruftbot.urls import *

development_patterns = [path("__debug__/", include(debug_toolbar.urls))]

urlpatterns.extend(development_patterns)
