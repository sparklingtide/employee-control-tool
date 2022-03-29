from emt.employees.models import Employee
from emt.providers.testprovider.models import TestResource


class TestEmployee:
    def test_create(self, root_group):
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")

        assert root_group.contains(employee)

    def test_add_perm_if_does_not_have_perm_yet(self):
        test_resource = TestResource.objects.create(name="test")
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")

        employee.add_perm(source=None, resource=test_resource)

        assert employee.has_perm(test_resource)
        assert test_resource.has_access_by(employee)

    def test_add_perm_if_has_perm(self, root_group):
        test_resource = TestResource.objects.create(name="test")
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")
        employee.add_perm(source=root_group, resource=test_resource)

        employee.add_perm(source=None, resource=test_resource)

        assert employee.has_perm(test_resource)
        assert test_resource.has_access_by(employee)

    def test_remove_perm_if_only_one_source_for_perm(self):
        test_resource = TestResource.objects.create(name="test")
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")
        employee.add_perm(source=None, resource=test_resource)

        employee.revoke_perm(source=None, resource=test_resource)

        assert not employee.has_perm(test_resource)
        assert not test_resource.has_access_by(employee)

    def test_remove_perm_if_some_sources_for_perm(self, root_group):
        test_resource = TestResource.objects.create(name="test")
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")
        employee.add_perm(source=root_group, resource=test_resource)
        employee.add_perm(source=None, resource=test_resource)

        employee.revoke_perm(source=None, resource=test_resource)

        assert employee.has_perm(test_resource)
        assert test_resource.has_access_by(employee)

    def test_deactivate(self):
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")
        test_resource = TestResource.objects.create(name="test")
        employee.add_perm(source=None, resource=test_resource)

        employee.deactivate()

        assert not employee.is_active
        assert not test_resource.has_access_by(employee)

    def test_activate(self):
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")
        test_resource = TestResource.objects.create(name="test")
        employee.add_perm(source=None, resource=test_resource)
        employee.deactivate()

        employee.activate()

        assert employee.is_active
        assert test_resource.has_access_by(employee)
