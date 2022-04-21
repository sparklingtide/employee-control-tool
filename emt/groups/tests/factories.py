import factory

from emt.core.tests.utils.factories import CustomDjangoModelFactory

from ..models import Group


class GroupFactory(CustomDjangoModelFactory):
    name = factory.Faker("word")

    class Meta:
        model = Group
