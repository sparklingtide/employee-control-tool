from django.urls import path

from . import views

urlpatterns = [
    path("", views.GroupListView.as_view()),
    path("<int:pk>/", views.GroupDetailView.as_view()),
    path("<int:pk>/add-employee/", views.GroupAddEmployeeView.as_view()),
    path("<int:pk>/remove-employee/", views.GroupRemoveEmployeeView.as_view()),
    path("<int:pk>/add-resource/", views.GroupAddResourceView.as_view()),
    path("<int:pk>/remove-resource/", views.GroupRemoveResourceView.as_view()),
]
