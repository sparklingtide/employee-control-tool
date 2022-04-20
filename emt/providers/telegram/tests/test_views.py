import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from emt.employees.tests.factories import EmployeeModelFactory
from emt.groups.tests.factories import GroupModelFactory

from .factories import TelegramModelFactory


@pytest.fixture
def telegram(telegram_client):
    group = GroupModelFactory()
    employee = EmployeeModelFactory()
    telegram = TelegramModelFactory()
    group.add_employee(employee)
    group.add_resource(telegram)

    yield telegram


class TestTelegramViews:
    url_list = reverse("telegram-list")
    data = {"name": "test_name"}

    @staticmethod
    def url_detail(telegram):
        return reverse("telegram-detail", args=[telegram.telegram.id])

    def test_list(self, admin_client, telegram, setup_user) -> None:
        admin_client.force_login(setup_user)
        response = admin_client.get(self.url_list)

        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]["id"] == telegram.id

    def test_detail(self, admin_client, telegram, setup_user) -> None:
        admin_client.force_login(setup_user)
        response = admin_client.get(self.url_detail)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == telegram.id

    def test_create(self, admin_client, telegram, setup_user) -> None:
        admin_client.force_login(setup_user)
        response = admin_client.post(self.url_list, data=self.data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == self.data["name"]

    def test_partial_update(self, admin_client, telegram, setup_user) -> None:
        admin_client.force_login(setup_user)
        response = admin_client.patch(self.url_detail, data=self.data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == self.data["name"]

    def test_update(self, admin_client, telegram, setup_user) -> None:
        admin_client.force_login(setup_user)
        response = admin_client.put(self.url_detail, data=self.data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == self.data["name"]
