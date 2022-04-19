import factory
from ..models import Group
from emt.core.tests.utils.factories import CustomDjangoModelFactory


class GroupModelFactory(CustomDjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = Group
