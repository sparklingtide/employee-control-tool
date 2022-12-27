from emt.core.drf.views.common import MappedModelViewSet
from emt.core.drf.views.constants import DEFAULT

from .models import Monday
from .serializers import MondaySerializer


class MondayViewSet(MappedModelViewSet):
    queryset = Monday.objects.all()
    serializer_class = {
        DEFAULT: MondaySerializer,
    }
