import hvac
from django.core.mail import EmailMessage
from django.db import models
from django.template.loader import render_to_string
from transliterate import translit

from emt.providers.models import Resource


class OpenVPN(Resource):
    openvpn_host = models.CharField(max_length=100)
    openvpn_port = models.PositiveIntegerField(default=1194)
    vault_url = models.CharField(max_length=100)
    vault_approle_role_id = models.CharField(max_length=100)
    vault_approle_secret_id = models.CharField(max_length=100)
    vault_pki_role_name = models.CharField(max_length=100, default="client")
    vault_pki_mount_point = models.CharField(max_length=100, default="pki")
    vault_kv_mount_point = models.CharField(max_length=100, default="kv")
    ta_key = models.TextField()

    @classmethod
    def create(self, **kwargs):
        openvpn = OpenVPN(**kwargs)
        openvpn.ta_key = openvpn._pull_ta_key()
        openvpn.save()
        return openvpn

    def give_access(self, employee):
        client = self._get_hvac()
        common_name = self._generate_common_name(employee)
        response = client.secrets.pki.generate_certificate(
            name=self.vault_pki_role_name,
            common_name=common_name,
            mount_point=self.vault_pki_mount_point,
        )
        self.clients.create(
            employee=employee,
            common_name=common_name,
            serial_number=response["data"]["serial_number"],
        )
        self._send_access_mail(
            employee,
            common_name,
            response["data"]["private_key"],
            response["data"]["certificate"],
            response["data"]["issuing_ca"],
        )

    def revoke_access(self, employee):
        openvpn_client = self.clients.get(employee=employee)
        client = self._get_hvac()
        client.secrets.pki.revoke_certificate(
            serial_number=openvpn_client.serial_number
        )
        openvpn_client.delete()

    def generate_config(self, employee):
        openvpn_client = self.clients.get(employee=employee)
        return openvpn_client.common_name, render_to_string(
            "providers/openvpn/client.ovpn",
            {
                "openvpn_host": self.openvpn_host,
                "openvpn_port": self.openvpn_port,
                "issuing_ca": openvpn_client.issuing_ca,
                "tls_auth": self.ta_key,
                "certificate": openvpn_client.certificate,
                "private_key": openvpn_client.private_key,
            },
        )

    def _generate_config(self, private_key, certificate, issuing_ca):
        return render_to_string(
            "providers/openvpn/client.ovpn",
            {
                "openvpn_host": self.openvpn_host,
                "openvpn_port": self.openvpn_port,
                "issuing_ca": issuing_ca,
                "tls_auth": self.ta_key,
                "certificate": certificate,
                "private_key": private_key,
            },
        )

    def _generate_common_name(self, employee):
        t_first_name = translit(employee.first_name, "ru", reversed=True)
        t_last_name = translit(employee.last_name, "ru", reversed=True)
        return f"{t_last_name.lower()}-{t_first_name.lower()[0]}"

    def _pull_ta_key(self):
        client = self._get_hvac()
        ta_key_result = client.secrets.kv.v1.read_secret(
            path="ta_key",
            mount_point=self.vault_kv_mount_point,
        )
        return ta_key_result["data"]["content"]

    def _send_access_mail(
        self, employee, common_name, private_key, certificate, issuing_ca
    ):
        config = self._generate_config(private_key, certificate, issuing_ca)
        mail = EmailMessage(
            "Доступ к корпоративному VPN",
            "Вы получили доступ к OpenVPN. Инструкцию по установке "
            "можно найти на сайте https://openvpn.net/vpn-client/. "
            "Файл конфигурации, который необходимо передать OpenVPN Connect, "
            "во вложении",
            to=[employee.email],
            attachments=[(f"{common_name}.ovpn", config, "text/plain")],
        )
        mail.send()

    def _get_hvac(self):
        client = hvac.Client(url=self.vault_url)
        client.auth.approle.login(
            role_id=self.vault_approle_role_id,
            secret_id=self.vault_approle_secret_id,
        )
        return client


class OpenVPNClient(Resource):
    vpn = models.ForeignKey("OpenVPN", on_delete=models.PROTECT, related_name="clients")
    employee = models.ForeignKey("employees.Employee", on_delete=models.PROTECT)
    common_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)

    class Meta:
        unique_together = ("vpn", "employee")
