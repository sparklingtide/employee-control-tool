from rest_framework import serializers

from emt.employees.models import Employee
from emt.providers.models import Resource

from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name", "parent")


class GroupEmployeeIdSerializer(serializers.Serializer):
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())


class GroupResourceIdSerializer(serializers.Serializer):
    resource_id = serializers.PrimaryKeyRelatedField(queryset=Resource.objects.all())
