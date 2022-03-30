from django.db import models

from emt.groups.models import Group
from emt.utils.choices import count_max_length


class Employee(models.Model):
    class OS(models.TextChoices):
        WINDOWS = "windows"
        LINUX = "linux"
        MAC_OS = "mac_os"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    os = models.CharField(max_length=count_max_length(OS), choices=OS.choices)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def create(cls, **kwargs):
        employee = Employee.objects.create(**kwargs)
        root_group = Group.get_root()
        root_group.add_employee(employee)
        return employee

    def deactivate(self):
        for perm in self.permissions.all():
            perm.resource.revoke_access(self)
        self.is_active = False
        self.save()

    def activate(self):
        for perm in self.permissions.all():
            perm.resource.give_access(self)
        self.is_active = True
        self.save()

    def add_perm(self, source, resource):
        # todo: неактивированный пользователь не получает доступ
        if not self.has_perm(resource):
            resource.give_access(self)
        self.permissions.create(source=source, resource=resource)

    def revoke_perm(self, source, resource):
        self.permissions.filter(source=source, resource=resource).delete()
        if not self.has_perm(resource):
            resource.revoke_access(self)

    def has_perm(self, resource):
        return self.permissions.filter(resource=resource).exists()


class Permission(models.Model):
    source = models.ForeignKey(
        "groups.Group",
        null=True,
        on_delete=models.PROTECT,
        related_name="given_permissions",
    )
    resource = models.ForeignKey(
        "providers.Resource", on_delete=models.PROTECT, related_name="+"
    )
    employee = models.ForeignKey(
        "employees.Employee", on_delete=models.PROTECT, related_name="permissions"
    )

    class Meta:
        unique_together = ("source", "resource", "employee")
