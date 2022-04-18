from django.urls import path

from . import views

urlpatterns = [
    path("", views.TelegramListView.as_view()),
    path("<int:pk>/", views.TelegramDetailView.as_view()),
]
