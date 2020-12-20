import actstream.urls
from django.urls import include
from django.urls import path


urlpatterns = [path("activity/", include(actstream.urls))]
