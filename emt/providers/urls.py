from django.urls import include, path

urlpatterns = [
    path("openvpn/", include("emt.providers.openvpn_vault.urls")),
    path("telegram/", include("emt.providers.telegram.urls")),
    path("gitlab/", include("emt.providers.gitlab.urls")),
]
