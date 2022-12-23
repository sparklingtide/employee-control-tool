import os

from django.conf import settings
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


class Command(BaseCommand):
    help = "Retrieve auth token for Telegram"

    TELEGRAM_API_ID = "app_id"
    TELEGRAM_API_HASH = "app_hash"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--id",
            dest=self.TELEGRAM_API_ID,
            help="API id for telegram app",
            default=settings.TELEGRAM_API_ID,
        )
        parser.add_argument(
            "--hash",
            dest=self.TELEGRAM_API_HASH,
            help="API hash for telegram app",
            default=settings.TELEGRAM_API_HASH,
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        with TelegramClient(
            "generator",
            options[self.TELEGRAM_API_ID],
            options[self.TELEGRAM_API_HASH],
        ) as client:
            auth_key = StringSession.save(client.session)

            self.stdout.write(self.style.SUCCESS(f"Your auth key: {auth_key}"))

        os.remove("generator.session")
