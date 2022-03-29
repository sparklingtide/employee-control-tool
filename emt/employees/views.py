from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def perform_create(self, serializer):
        return Employee.create(**serializer.validated_data)


class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDeactivateView(generics.GenericAPIView):
    queryset = Employee.objects.all()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT))
    def post(self, request, *args, **kwargs):
        employee = self.get_object()
        employee.deactivate()
        return Response(status=200)


class EmployeeActivateView(generics.GenericAPIView):
    queryset = Employee.objects.all()

    @swagger_auto_schema(request_body=openapi.Schema(type=openapi.TYPE_OBJECT))
    def post(self, request, *args, **kwargs):
        employee = self.get_object()
        employee.activate()
        return Response(status=200)
