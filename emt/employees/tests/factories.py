import factory

from emt.core.tests.utils.factories import CustomDjangoModelFactory
from emt.groups.tests.factories import GroupFactory

from ..models import Employee, Permission


class EmployeeFactory(CustomDjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    telegram = factory.Faker("word")

    class Meta:
        model = Employee


class PermissionFactory(CustomDjangoModelFactory):
    source = factory.SubFactory(GroupFactory)
    employee = factory.SubFactory(EmployeeFactory)

    class Meta:
        model = Permission
