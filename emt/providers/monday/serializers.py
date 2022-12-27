from rest_framework import serializers

from .models import Monday


class MondaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monday
        fields = ["id", "name", "board_id"]
