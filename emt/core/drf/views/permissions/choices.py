from .meta import MetaPermission


class All(MetaPermission):
    """
    Meta permission.

    Allows access when all permissions passed in its constructor has
    permission
    """
    def _check_permission(self, method_name, *args):
        return all(
            (getattr(permission(), method_name)(*args)
             for permission in self.permissions)
        )

    def has_permission(self, request, view):
        return self._check_permission('has_permission', request, view)

    def has_object_permission(self, request, view, obj):
        return self._check_permission(
            'has_object_permission', request, view, obj
        )


class AnyOf(MetaPermission):
    """
    Meta permission.

    Allows access when any of permissions passed in its constructor has
    permission
    """

    def __init__(self, *permissions):
        super(AnyOf, self).__init__(*permissions)
        self.allowed_permissions = []

    def has_permission(self, request, view):
        results = []
        self.allowed_permissions = []
        for permission in self.permissions:
            has_permission = permission().has_permission(request, view)
            results.append(has_permission)
            if not has_permission:
                continue
            self.allowed_permissions.append(permission)

        return any(results)

    def has_object_permission(self, request, view, obj):
        return any(
            (permission().has_object_permission(request, view, obj)
             for permission in self.allowed_permissions)
        )
