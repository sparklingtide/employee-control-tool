import factory
from ..models import Telegram
from emt.core.tests.utils.factories import CustomDjangoModelFactory


class TelegramModelFactory(CustomDjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = Telegram
