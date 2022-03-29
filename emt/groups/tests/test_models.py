from emt.employees.models import Employee
from emt.groups.models import Group
from emt.providers.testprovider.models import TestResource


class TestGroup:
    def test_add_employee(self, root_group):
        group_1 = Group.objects.create(name="group 1", parent=root_group)
        resource_1 = TestResource.objects.create(name="test 1")
        group_1.add_resource(resource_1)
        group_2 = Group.objects.create(name="group 2", parent=group_1)
        resource_2 = TestResource.objects.create(name="test 2")
        group_2.add_resource(resource_2)
        group_3 = Group.objects.create(name="group 3", parent=group_2)
        resource_3 = TestResource.objects.create(name="test 3")
        group_3.add_resource(resource_3)
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")

        group_2.add_employee(employee)

        assert group_2.contains(employee)
        assert group_1.contains(employee)
        assert not group_3.contains(employee)
        assert employee.has_perm(resource_1)
        assert employee.has_perm(resource_2)
        assert not employee.has_perm(resource_3)

    def test_add_employee_if_he_is_in_parent_group(self, root_group):
        group_1 = Group.objects.create(name="group 1", parent=root_group)
        resource_1 = TestResource.objects.create(name="test 1")
        group_1.add_resource(resource_1)
        group_2 = Group.objects.create(name="group 2", parent=group_1)
        resource_2 = TestResource.objects.create(name="test 2")
        group_2.add_resource(resource_2)
        group_3 = Group.objects.create(name="group 3", parent=group_2)
        resource_3 = TestResource.objects.create(name="test 3")
        group_3.add_resource(resource_3)
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")
        group_1.add_employee(employee)

        group_2.add_employee(employee)

        assert group_2.contains(employee)
        assert group_1.contains(employee)
        assert not group_3.contains(employee)
        assert employee.has_perm(resource_1)
        assert employee.has_perm(resource_2)
        assert not employee.has_perm(resource_3)

    def test_remove_employee(self, root_group):
        group_1 = Group.objects.create(name="group 1", parent=root_group)
        resource_1 = TestResource.objects.create(name="test 1")
        group_1.add_resource(resource_1)
        group_2 = Group.objects.create(name="group 2", parent=group_1)
        resource_2 = TestResource.objects.create(name="test 2")
        group_2.add_resource(resource_2)
        group_3 = Group.objects.create(name="group 3", parent=group_2)
        resource_3 = TestResource.objects.create(name="test 3")
        group_3.add_resource(resource_3)
        employee = Employee.create(first_name="Ivan", last_name="Ivanov")
        group_2.add_employee(employee)

        group_2.remove_employee(employee)

        assert not group_2.contains(employee)
        assert group_1.contains(employee)
        assert not group_3.contains(employee)
        assert employee.has_perm(resource_1)
        assert not employee.has_perm(resource_2)
        assert not employee.has_perm(resource_3)

    def test_add_resource(self, root_group):
        group_1 = Group.objects.create(name="group 1", parent=root_group)
        group_2 = Group.objects.create(name="group 2", parent=group_1)
        group_3 = Group.objects.create(name="group 3", parent=group_2)
        employee_1 = Employee.create(first_name="Ivan", last_name="Ivanov")
        group_2.add_employee(employee_1)
        employee_2 = Employee.create(first_name="Petr", last_name="Petrov")
        group_3.add_employee(employee_2)
        resource = TestResource.objects.create(name="test")

        group_2.add_resource(resource)

        assert employee_1.has_perm(resource)
        assert employee_2.has_perm(resource)
