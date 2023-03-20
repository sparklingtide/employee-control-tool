from rest_framework import serializers

from .models import Discord


class DiscordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discord
        fields = (
            "id",
            "name",
            "server_id",
        )
