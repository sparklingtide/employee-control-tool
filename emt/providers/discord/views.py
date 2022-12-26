from emt.core.drf.views.common import MappedModelViewSet
from emt.providers.discord.client import DiscordClient
from emt.providers.discord.models import Discord
from emt.core.drf.views.constants import DEFAULT
from emt.providers.discord.serializers import DiscordSerializer


class TelegramViewSet(MappedModelViewSet):
    queryset = Discord.objects.all()
    serializer_class = {
        DEFAULT: DiscordSerializer,
    }
