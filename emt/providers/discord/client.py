import requests
from django.conf import settings


class DiscordClient:
    api: str = settings.DISCORD_API
    headers: dict = {'Authorization': f'Bot {settings.DISCORD_TOKEN}'}

    def __init__(self, server: int):
        self.server = server

    def get_member_by_username(self, username):
        response = requests.get(f'{self.api}/guilds/{self.server}/members/search?query={username}',
                                headers=self.headers)
        try:
            return response.json()[0]
        except (KeyError, IndexError):
            raise Exception(f'Пользователь {username} не найден на сервере')

    def kick_member(self, user_id):
        response = requests.delete(f'{self.api}/guilds/{self.server}/members/{user_id}',
                                   headers=self.headers)

        return response.status_code == 204
