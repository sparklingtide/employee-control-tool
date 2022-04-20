import factory

from emt.core.tests.utils.factories import CustomDjangoModelFactory

from ..models import Group


class GroupModelFactory(CustomDjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = Group
