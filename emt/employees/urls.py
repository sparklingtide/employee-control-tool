from django.urls import path

from . import views

urlpatterns = [
    path("", views.EmployeeListView.as_view()),
    path("<int:pk>/", views.EmployeeDetailView.as_view()),
    path("<int:pk>/deactivate/", views.EmployeeDeactivateView.as_view()),
    path("<int:pk>/activate/", views.EmployeeActivateView.as_view()),
]
