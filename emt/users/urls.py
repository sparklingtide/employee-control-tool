from django.urls import path

from . import views

urlpatterns = [
    path("token/", views.DecoratedTokenObtainPairView.as_view()),
    path("token/refresh/", views.DecoratedTokenRefreshView.as_view()),
]
