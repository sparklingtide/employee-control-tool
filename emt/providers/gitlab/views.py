from emt.core.drf.views.common import MappedModelViewSet
from emt.core.drf.views.constants import DEFAULT

from .models import Gitlab
from .serializers import GitlabSerializer


class GitlabViewSet(MappedModelViewSet):
    queryset = Gitlab.objects.all()
    serializer_class = {
        DEFAULT: GitlabSerializer,
    }
