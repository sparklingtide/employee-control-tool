import os

from django.core.management import BaseCommand
from django.core.management.base import CommandError, CommandParser
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


class Command(BaseCommand):
    help = "Retrieve auth token for Telegram"

    TELEGRAM_API_ID = "app_id"
    TELEGRAM_API_HASH = "app_hash"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-i",
            "--id",
            dest=self.TELEGRAM_API_ID,
            nargs="+",
            help="API id for telegram app",
        )
        parser.add_argument(
            "-h",
            "--hash",
            dest=self.TELEGRAM_API_HASH,
            nargs="+",
            help="API hash for telegram app",
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        if not all(
            (
                options[self.TELEGRAM_API_ID],
                options[self.TELEGRAM_API_HASH],
            )
        ):
            raise CommandError(
                f"Specify {self.TELEGRAM_API_ID} and {self.TELEGRAM_API_HASH}"
            )

        with TelegramClient(
            "generator",
            options[self.TELEGRAM_API_ID],
            options[self.TELEGRAM_API_HASH],
        ) as client:
            auth_key = StringSession.save(client.session)

            self.stdout.write(self.style.SUCCESS(f"Your auth key: {auth_key}"))

        os.remove("generator.session")
