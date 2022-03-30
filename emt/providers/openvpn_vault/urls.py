from django.urls import path

from . import views

urlpatterns = [
    path("", views.OpenVPNListView.as_view()),
    path("<int:pk>/", views.OpenVPNDetailView.as_view()),
    path("<int:pk>/reset-config/", views.OpenVPNResetConfigView.as_view()),
]
