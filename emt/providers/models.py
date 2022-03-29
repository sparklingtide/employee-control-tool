from django.db import models
from polymorphic.models import PolymorphicModel


class Resource(PolymorphicModel):
    name = models.CharField(max_length=100)

    def give_access(self, employee):
        raise NotImplementedError

    def revoke_access(self, employee):
        raise NotImplementedError
