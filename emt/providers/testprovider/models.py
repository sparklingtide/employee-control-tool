from django.db import models

from emt.providers.models import Resource


class TestResource(Resource):
    def give_access(self, employee):
        self.entries.create(employee=employee)

    def revoke_access(self, employee):
        self.entries.filter(employee=employee).delete()

    def has_access_by(self, employee):
        return self.entries.filter(employee=employee).exists()


class TestResourceEntry(models.Model):
    resource = models.ForeignKey(
        "testprovider.TestResource", on_delete=models.PROTECT, related_name="entries"
    )
    employee = models.ForeignKey(
        "employees.Employee", on_delete=models.PROTECT, related_name="+"
    )

    class Meta:
        unique_together = ("resource", "employee")
