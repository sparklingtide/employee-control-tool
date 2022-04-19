import factory
from ..models import User
from emt.core.tests.utils.factories import CustomDjangoModelFactory


class UserModelFactory(CustomDjangoModelFactory):
    username = factory.Sequence(lambda n: f"username {n}")

    class Meta:
        model = User
