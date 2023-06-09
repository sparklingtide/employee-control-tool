import pytest
from rest_framework.test import APIClient

from emt.groups.models import Group
from emt.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def django_db(db):
    pass


@pytest.fixture(autouse=True)
def root_group():
    return Group.objects.create(name="Компания")


@pytest.fixture(autouse=True)
def telegram_client(mocker):
    client = mocker.Mock()
    chat = mocker.Mock()
    chat.id = 111
    client.chats = [chat]

    yield mocker.patch("django.conf.settings.TELEGRAM_API_CLIENT", return_value=client)


@pytest.fixture(autouse=True)
def setup_user():
    user = UserFactory()
    user.set_password("1")
    user.save()
    return user


@pytest.fixture(autouse=True)
def api_client(setup_user):
    client = APIClient()
    client.force_authenticate(setup_user)
    return client
