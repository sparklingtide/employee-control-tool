from django.core.management import BaseCommand

from emt.groups.models import Group


class Command(BaseCommand):
    help = "Initialize the app"

    def handle(self, *args, **options):
        self._create_root_group()
        self.stdout.write(self.style.SUCCESS("Successfully initialized."))

    def _create_root_group(self):
        Group.objects.create(name="Компания")
