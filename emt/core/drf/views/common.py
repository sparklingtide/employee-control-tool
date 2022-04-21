from rest_framework.viewsets import ModelViewSet

from .mixins.base import ActionToPermissionsMap, ActionToSerializerMap


class MappedModelViewSet(ActionToPermissionsMap, ActionToSerializerMap, ModelViewSet):
    pass
