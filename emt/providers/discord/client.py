import requests
from django.conf import settings


class DiscordClient:
    api: str = settings.DISCORD_API
    headers: dict = {'Authorization': f'Bot {settings.DISCORD_TOKEN}',
                     'Content-Type': 'application/json'}
    guest_channel_name: str = settings.DISCORD_GUEST_CHANNEL_NAME

    def __init__(self, server: str):
        self.server = server

    def get_member_by_id(self, user_id) -> dict:
        response = requests.get(f'{self.api}/guilds/{self.server}/members/{user_id}',
                                headers=self.headers)
        response.raise_for_status()
        return response.json()

    def kick_member(self, user_id) -> bool:
        response = requests.delete(f'{self.api}/guilds/{self.server}/members/{user_id}',
                                   headers=self.headers)

        return response.status_code == 204

    def create_invite(self, channel_id: str = None, max_uses: int = 1) -> dict:
        channel_id = channel_id or self.common_channel['id']
        response = requests.post(f'{self.api}/channels/{channel_id}/invites',
                                 headers=self.headers,
                                 json={'unique': True,
                                       'max_age': 604800,
                                       'max_uses': max_uses})

        return response.json()

    def delete_invite(self, code: str) -> bool:
        response = requests.delete(f'{self.api}/invites/{code}',
                                   headers=self.headers)

        return response.status_code == 204

    def get_channels(self, guild_id: str) -> dict:
        response = requests.get(f'{self.api}/guilds/{guild_id}/channels',
                                headers=self.headers)

        return response.json()

    @property
    def common_channel(self) -> dict:
        channels = self.get_channels(self.server)
        return [channel for channel in channels
                if channel['parent_id']
                and channel['type'] == 0
                and channel['name'] == self.guest_channel_name][0]
