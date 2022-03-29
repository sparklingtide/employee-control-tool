import pytest

from emt.groups.models import Group


@pytest.fixture(autouse=True)
def django_db(db):
    pass


@pytest.fixture(autouse=True)
def root_group():
    return Group.objects.create(name="Компания")
