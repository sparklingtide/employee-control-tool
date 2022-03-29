from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("api/", include("emt.users.urls")),
    path("api/employees/", include("emt.employees.urls")),
    path("api/groups/", include("emt.groups.urls")),
    path("api/providers/", include("emt.providers.urls")),
    path("api/docs/", include("emt.swagger.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
