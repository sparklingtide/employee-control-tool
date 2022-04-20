from rest_framework.permissions import BasePermission, IsAuthenticated


class AllowNobody(BasePermission):
    def has_permission(self, request, view):
        return False


class BaseIsOwner(IsAuthenticated):
    def check_user_is_object_creator(self, request, view, obj, user=None):
        assert hasattr(obj, "user")

        user = request.user if user is None else user
        return obj.user == user


class UserPropertyPermission(IsAuthenticated):
    def _get_user(self, request, view):
        return request.user

    def has_permission(self, request, view):
        return super(UserPropertyPermission, self).has_permission(
            request, view
        ) and getattr(self._get_user(request, view), self.property_name, False)


class UserDoesNotHaveProperty(UserPropertyPermission):
    def has_permission(self, request, view):
        return not super(UserDoesNotHaveProperty, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return not super(UserDoesNotHaveProperty, self).has_object_permission(
            request, view
        )
