from rest_framework.permissions import BasePermission

from .base import BaseIsOwner, UserPropertyPermission


class IsAnonymous(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return not request.user.is_authenticated
        return False


class IsAuthor(BaseIsOwner):
    """
    Checking if current user is creator of an object.
    Overrides 'has_object_permission' for checking creator.
    """

    def has_object_permission(self, request, view, obj):
        return self.check_user_is_object_creator(request, view, obj)


class IsSuperUser(UserPropertyPermission):
    property_name = "is_superuser"


class IsRequestUser(BasePermission):
    message = "The user in the request and in the parameters must be the same."

    def has_permission(self, request, view):
        resource_user_pk = view.kwargs.get("parent_lookup_user")
        if resource_user_pk is None:
            resource_user_pk = view.kwargs.get("parent_lookup_family__user")
        return str(request.user.id) == resource_user_pk
