from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Group(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", related_name="children", on_delete=models.PROTECT, null=True
    )
    resources = models.ManyToManyField("providers.Resource", related_name="+")
    employees = models.ManyToManyField("employees.Employee", related_name="groups")

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name

    def add_employee(self, employee):
        if self.contains(employee):
            return
        self.employees.add(employee)
        for resource in self.resources.all():
            employee.add_perm(source=self, resource=resource)
        if self.parent is not None:
            self.parent.add_employee(employee)

    def remove_employee(self, employee):
        for child in self.children.all():
            child.remove_employee(employee)
        for resource in self.resources.all():
            employee.revoke_perm(source=self, resource=resource)
        self.employees.remove(employee)

    def add_resource(self, resource):
        self.resources.add(resource)
        for employee in self.employees.all():
            employee.add_perm(source=self, resource=resource)

    def remove_resource(self, resource):
        for employee in self.employees.all():
            employee.revoke_perm(source=self, resource=resource)
        self.resources.remove(resource)

    @classmethod
    def get_root(self):
        return Group.objects.get(parent=None)

    def contains(self, employee):
        return employee in self.employees.all()
