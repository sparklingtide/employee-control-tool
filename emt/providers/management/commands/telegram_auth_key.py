import os

from django.conf import settings
from django.core.management import BaseCommand
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


class Command(BaseCommand):
    help = "Retrieve auth token for Telegram"

    def handle(self, *args, **options):
        with TelegramClient(
            "generator",
            settings.TELEGRAM_API_ID,
            settings.TELEGRAM_API_HASH,
        ) as client:
            auth_key = StringSession.save(client.session)

            self.stdout.write(self.style.SUCCESS(f"Your auth key: {auth_key}"))

        os.remove("generator.session")
