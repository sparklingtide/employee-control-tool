import asyncio

from telethon.sync import TelegramClient
from django.conf import settings
from telethon.sessions import StringSession


class TelethonClient:
    client: TelegramClient = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, 'client'):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(
                StringSession(settings.TELEGRAM_STRING_SESSION),
                settings.TELEGRAM_API_ID,
                settings.TELEGRAM_API_HASH,
            )
            client.connect()
            cls.client = client
        return cls.client

    def __call__(self, *args, **kwargs):
        self.client(*args, **kwargs)
