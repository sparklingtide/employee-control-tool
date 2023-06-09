from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "telegram",
            "gitlab_username",
            "discord_id",
            "is_active",
        ]
        read_only_fields = ["id", "is_active"]
