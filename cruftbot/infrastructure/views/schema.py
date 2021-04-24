"""Open API browser."""
from drf_yasg.openapi import Contact
from drf_yasg.openapi import Info
from drf_yasg.openapi import License
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    Info(
        title="cruftbot",
        default_version="v1",
        description="Apply cruft tool continuously in pull requests",
        terms_of_service="https://github.com/proofit404/cruftbot/",
        contact=Contact(email="proofit404@gmail.com"),
        license=License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)
