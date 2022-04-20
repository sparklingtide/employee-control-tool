from unittest.mock import Mock, patch

from django.test import TestCase

from emt.employees.models import Permission
from emt.employees.tests.factories import EmployeeModelFactory
from emt.groups.models import Group
from emt.groups.tests.factories import GroupModelFactory
from emt.users.tests.factories import UserModelFactory

from ..models import Telegram
from .mock import mocked_client


class TelegramResourceTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = UserModelFactory()
        cls.group = GroupModelFactory()
        cls.employee = EmployeeModelFactory()
        cls.group.add_employee(cls.employee)

    @patch(
        "emt.providers.telegram.models.Telegram._get_client", return_value=mocked_client
    )
    def test_create_method(self, client: Mock) -> None:
        telegram = Telegram.create(
            name="test_group",
        )
        self.assertEqual(telegram.group_id, 111)

    @patch(
        "emt.providers.telegram.models.Telegram._get_client", return_value=mocked_client
    )
    def test_give_and_revoke_access(self, client: Mock) -> None:
        telegram = Telegram.create(
            name="test_group",
        )

        # Check there is a request for base users after resource creation
        self.assertEqual(client.call_count, 1)

        self.group.add_resource(telegram)

        # Check there is a request for employee after resource assignment
        self.assertEqual(client.call_count, 2)

        permission_qs = Permission.objects.filter(
            source=self.group,
            resource=telegram,
            employee=self.employee,
        )

        self.assertTrue(permission_qs.exists())

        self.group.remove_resource(telegram)

        # Check there is a request for employee after resource removal
        self.assertEqual(client.call_count, 3)

        group_qs = Group.objects.filter(
            resources__in=[telegram],
            employees__in=[self.employee],
        )

        self.assertFalse(group_qs.exists())
        self.assertFalse(permission_qs.exists())
