from django.contrib import admin
from rest_framework.schemas import get_schema_view
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("users_api.urls", namespace="users_api")),
    path("api/v1/buildings/", include("buildings_api.urls", namespace="buildings_api")),
    path("api/v1/events/", include("events_api.urls", namespace="events_api")),
    
    # API schema and Documentation
    path('schema/docs/', include_docs_urls(title='Cola')),
    path(
        "schema",
        get_schema_view(
            title="Cola", description="API for the Cola", version="1.0.0"
        ),
        name="openapi-schema",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
