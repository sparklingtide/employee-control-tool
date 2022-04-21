import pytest

from emt.employees.tests.factories import EmployeeFactory

from ..models import Telegram


@pytest.mark.django_db
class TestTelegramModels:
    def test_create_method(self, telegram_client) -> None:
        telegram = Telegram.create(
            name="test_group",
        )
        assert telegram.group_id == 111

    def test_give_and_revoke_access(self, telegram_client, root_group) -> None:
        employee = EmployeeFactory()
        root_group.add_employee(employee)
        telegram = Telegram.create(
            name="test_group",
        )

        # Check there is a request for base users after resource creation
        assert telegram_client.call_count == 1

        telegram.give_access(employee)

        # Check there is a request for employee after resource assignment
        assert telegram_client.call_count == 2

        telegram.revoke_access(employee)

        # Check there is a request for employee after resource removal
        assert telegram_client.call_count == 3
