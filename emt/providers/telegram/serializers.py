from rest_framework import serializers

from .models import Telegram


class TelegramSerializer(serializers.ModelSerializer):
    group_id = serializers.ReadOnlyField()

    class Meta:
        model = Telegram
        fields = (
            "id",
            "name",
            "group_id",
        )
