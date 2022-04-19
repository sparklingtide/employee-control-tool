from ..utils import get_view_attr


class ActionToPermissionsMap(object):
    def get_permissions(self):
        permission_classes = get_view_attr(self, 'permission_classes')
        return [permission() for permission in permission_classes]


class ActionToSerializerMap(object):
    def get_serializer_class(self):
        serializer_class = get_view_attr(self, 'serializer_class')
        assert serializer_class is not None, (
            f"'{self.__class__.__name__}' should have a 'serializer_class' "
            "attribute or override the 'get_serializer_class'."
        )
        return serializer_class
