from django.urls import include, path

urlpatterns = [
    path("openvpn/", include("emt.providers.openvpn_vault.urls")),
]
