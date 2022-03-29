from rest_framework import serializers

from emt.employees.models import Employee

from .models import OpenVPN


class OpenVPNSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenVPN
        fields = (
            "id",
            "openvpn_host",
            "openvpn_port",
            "vault_url",
            "vault_approle_role_id",
            "vault_approle_secret_id",
            "vault_pki_role_name",
            "vault_pki_mount_point",
            "vault_kv_mount_point",
            "ta_key",
        )
        extra_kwargs = {"vault_approle_secret_id": {"write_only": True}}


class OpenVPNEmployeeIdSerializer(serializers.Serializer):
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
