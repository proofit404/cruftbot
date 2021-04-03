import actstream.urls
import allauth.urls
from django.urls import include
from django.urls import path

from cruftbot.infrastructure.views.index import index
from cruftbot.infrastructure.views.schema import schema_view

urlpatterns = [
    path("accounts/", include(allauth.urls)),
    path("activity/", include(actstream.urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("", index),
]
