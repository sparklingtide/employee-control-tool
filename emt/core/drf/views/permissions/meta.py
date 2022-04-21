from rest_framework.permissions import BasePermission


class MetaPermission(BasePermission):
    def __init__(self, *permissions):
        self.permissions = permissions

    def __copy__(self):
        return type(self)(*self.permissions)

    def __call__(self):
        return self

    def __iter__(self):
        yield self
