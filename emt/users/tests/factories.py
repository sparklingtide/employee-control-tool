import factory

from emt.core.tests.utils.factories import CustomDjangoModelFactory

from ..models import User


class UserModelFactory(CustomDjangoModelFactory):
    username = factory.Sequence(lambda n: f"username {n}")

    class Meta:
        model = User
