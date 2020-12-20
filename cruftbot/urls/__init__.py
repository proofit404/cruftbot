import actstream.urls
from django.urls import include
from django.urls import path

from cruftbot.views.index import index


urlpatterns = [path("activity/", include(actstream.urls)), path("", index)]
