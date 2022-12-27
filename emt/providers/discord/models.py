from django.db import models

from emt.providers.discord.client import DiscordClient
from emt.providers.models import Resource


class Discord(Resource):
    server_id = models.PositiveIntegerField()

    def give_access(self, employee):
        ...

    def revoke_access(self, employee):
        if not employee.discord_id:
            return

        client = self._get_client(self.server_id)
        user = client.get_member_by_id(employee.discord_id)
        client.kick_member(user['user']['id'])

    @staticmethod
    def _get_client(server):
        client = DiscordClient(server)
        return client
