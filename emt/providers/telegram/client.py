import asyncio

from telethon import TelegramClient
from django.conf import settings


class TelethonClient:
    client: TelegramClient = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, 'client'):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = TelegramClient(
                settings.TELEGRAM_STRING_SESSION,
                settings.TELEGRAM_API_ID,
                settings.TELEGRAM_API_HASH,
                loop=loop
            )
            client.connect()
            cls.client = client
        return cls.client

    def __call__(self, *args, **kwargs):
        self.client(*args, **kwargs)
