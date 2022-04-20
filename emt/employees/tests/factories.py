import factory

from emt.core.tests.utils.factories import CustomDjangoModelFactory
from emt.groups.tests.factories import GroupModelFactory

from ..models import Employee, Permission


class EmployeeModelFactory(CustomDjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    telegram = factory.Faker("word")

    class Meta:
        model = Employee


class PermissionModelFactory(CustomDjangoModelFactory):
    source = factory.SubFactory(GroupModelFactory)
    employee = factory.SubFactory(EmployeeModelFactory)

    class Meta:
        model = Permission
