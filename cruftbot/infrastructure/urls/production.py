"""HTTP request routing for production environment."""
from django.urls import include
from django.urls import path

from cruftbot.infrastructure import views

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("activity/", include("actstream.urls")),
    path("health/", include("health_check.urls")),
    path("swagger/", views.schema.with_ui("swagger", cache_timeout=0)),
    path("", views.index),
]
