from emt.employees.models import Permission
from emt.employees.tests.factories import EmployeeModelFactory
from emt.groups.models import Group

from ..models import Telegram


class TestTelegramModels:
    def test_create_method(self, telegram_client) -> None:
        telegram = Telegram.create(
            name="test_group",
        )
        assert telegram.group_id == 111

    def test_give_and_revoke_access(self, telegram_client, root_group) -> None:
        employee = EmployeeModelFactory()
        root_group.add_employee(employee)
        telegram = Telegram.create(
            name="test_group",
        )

        # Check there is a request for base users after resource creation
        assert telegram_client.call_count == 1

        root_group.add_resource(telegram)

        # Check there is a request for employee after resource assignment
        assert telegram_client.call_count == 2

        permission_qs = Permission.objects.filter(
            source=root_group,
            resource=telegram,
            employee=employee,
        )

        assert permission_qs.exists()

        root_group.remove_resource(telegram)

        # Check there is a request for employee after resource removal
        assert telegram_client.call_count == 3

        group_qs = Group.objects.filter(
            resources__in=[telegram],
            employees__in=[employee],
        )

        assert not group_qs.exists()
        assert not permission_qs.exists()
