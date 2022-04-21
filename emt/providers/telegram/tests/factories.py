import factory

from emt.core.tests.utils.factories import CustomDjangoModelFactory

from ..models import Telegram


class TelegramFactory(CustomDjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = Telegram
