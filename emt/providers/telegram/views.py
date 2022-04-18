from rest_framework import generics

from .models import Telegram
from .serializers import TelegramSerializer


class TelegramListView(generics.ListCreateAPIView):
    queryset = Telegram.objects.all()
    serializer_class = TelegramSerializer

    def perform_create(self, serializer):
        serializer.instance = Telegram.create(**serializer.validated_data)
        return serializer.instance


class TelegramDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Telegram.objects.all()
    serializer_class = TelegramSerializer
