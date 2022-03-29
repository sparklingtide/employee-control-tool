from rest_framework import generics

from .models import OpenVPN
from .serializers import OpenVPNSerializer


class OpenVPNListView(generics.ListCreateAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer

    def perform_create(self, serializer):
        serializer.instance = OpenVPN.create(**serializer.validated_data)
        return serializer.instance


class OpenVPNDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer
