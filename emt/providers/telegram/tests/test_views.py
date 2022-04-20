from unittest.mock import Mock, patch

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from emt.employees.tests.factories import EmployeeModelFactory
from emt.groups.tests.factories import GroupModelFactory
from emt.users.tests.factories import UserModelFactory

from .factories import TelegramModelFactory
from .mock import mocked_client


class TelegramResourceTestCase(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = UserModelFactory()
        cls.group = GroupModelFactory()
        cls.employee = EmployeeModelFactory()
        cls.telegram = TelegramModelFactory()

        with patch(
            "emt.providers.telegram.models.Telegram._get_client",
            return_value=mocked_client,
        ):
            cls.group.add_employee(cls.employee)
            cls.group.add_resource(cls.telegram)

        cls.url_list = reverse("telegram-list")
        cls.url_detail = reverse("telegram-detail", args=[cls.telegram.id])
        cls.data = {"name": "test_name"}

    def test_list(self) -> None:
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], self.telegram.id)

    def test_detail(self) -> None:
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.telegram.id)

    @patch(
        "emt.providers.telegram.models.Telegram._get_client", return_value=mocked_client
    )
    def test_create(self, client: Mock) -> None:
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url_list, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], self.data["name"])

    @patch(
        "emt.providers.telegram.models.Telegram._get_client", return_value=mocked_client
    )
    def test_partial_update(self, client: Mock) -> None:
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url_detail, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.data["name"])

    @patch(
        "emt.providers.telegram.models.Telegram._get_client", return_value=mocked_client
    )
    def test_update(self, client: Mock) -> None:
        self.client.force_authenticate(self.user)
        response = self.client.put(self.url_detail, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.data["name"])
