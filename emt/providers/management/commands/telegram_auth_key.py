import os

from django.conf import settings
from django.core.management import BaseCommand
from telethon.sessions import StringSession


class Command(BaseCommand):
    help = "Retrieve auth token for Telegram"

    def handle(self, *args, **options):
        with settings.TELEGRAM_API_CLIENT(
            "generator",
            settings.TELEGRAM_API_ID,
            settings.TELEGRAM_API_HASH,
        ) as client:
            auth_key = StringSession.save(client.session)

            self.stdout.write(self.style.SUCCESS(f"Your auth key: {auth_key}"))

        os.remove("generator.session")
