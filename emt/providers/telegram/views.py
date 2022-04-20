from rest_framework.permissions import IsAuthenticated

from emt.core.drf.views.common import MappedModelViewSet
from emt.core.drf.views.constants import DEFAULT

from .models import Telegram
from .serializers import TelegramSerializer


class TelegramViewSet(MappedModelViewSet):
    queryset = Telegram.objects.all()
    serializer_class = {
        DEFAULT: TelegramSerializer,
    }
    permission_classes = {
        DEFAULT: (IsAuthenticated,),
    }

    def perform_create(self, serializer):
        serializer.instance = Telegram.create(**serializer.validated_data)
        return serializer.instance
