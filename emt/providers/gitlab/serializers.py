from rest_framework import serializers

from .models import Gitlab


class GitlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gitlab
        fields = (
            "id",
            "name",
            "project_id",
            "role",
        )
