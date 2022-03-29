from django.urls import path

from . import views

urlpatterns = [
    path("", views.OpenVPNListView.as_view()),
    path("<int:pk>/", views.OpenVPNDetailView.as_view()),
    path("<int:pk>/generate-config/", views.OpenVPNGenerateConfigView.as_view()),
]
