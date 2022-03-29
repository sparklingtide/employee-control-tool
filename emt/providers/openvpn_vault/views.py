from rest_framework import generics

from .models import OpenVPN
from .serializers import OpenVPNSerializer


class OpenVPNListView(generics.ListCreateAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer

    def perform_create(self, serializer):
        return OpenVPN.create(**serializer.validated_data)


class OpenVPNDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpenVPN.objects.all()
    serializer_class = OpenVPNSerializer
