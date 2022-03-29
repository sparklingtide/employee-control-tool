from rest_framework import generics
from rest_framework.response import Response

from .models import Group
from .serializers import (
    GroupEmployeeIdSerializer,
    GroupResourceIdSerializer,
    GroupSerializer,
)


class GroupListView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupAddEmployeeView(generics.GenericAPIView):
    serializer_class = GroupEmployeeIdSerializer
    queryset = Group.objects.all()

    def post(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data["employee_id"]
        group.add_employee(employee)
        return Response(status=200)


class GroupRemoveEmployeeView(generics.GenericAPIView):
    serializer_class = GroupEmployeeIdSerializer
    queryset = Group.objects.all()

    def post(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data["employee_id"]
        group.remove_employee(employee)
        return Response(status=200)


class GroupAddResourceView(generics.GenericAPIView):
    serializer_class = GroupResourceIdSerializer
    queryset = Group.objects.all()

    def post(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resource = serializer.validated_data["resource_id"]
        group.add_resource(resource)
        return Response(status=200)


class GroupRemoveResourceView(generics.GenericAPIView):
    serializer_class = GroupResourceIdSerializer
    queryset = Group.objects.all()

    def post(self, request, *args, **kwargs):
        group = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resource = serializer.validated_data["resource_id"]
        group.remove_resource(resource)
        return Response(status=200)
