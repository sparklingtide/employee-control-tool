from rest_framework import generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import OpenVPN
from .serializers import EmployeeIdSerializer, OpenVPNSerializer


class OpenVPNListView(generics.ListCreateAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer

    def perform_create(self, serializer):
        serializer.instance = OpenVPN.create(**serializer.validated_data)
        return serializer.instance


class OpenVPNDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer


class OpenVPNResetConfigView(generics.GenericAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = EmployeeIdSerializer

    @swagger_auto_schema(responses={200: openapi.Response("")})
    def post(self, request, *args, **kwargs):
        openvpn = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.validated_data["employee_id"]
        openvpn.reset_config(employee)
        return Response()
