import pytest

from emt.groups.models import Group
from emt.users.tests.factories import UserModelFactory


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
    user = UserModelFactory()
    user.set_password("1")
    user.save()
    return user
