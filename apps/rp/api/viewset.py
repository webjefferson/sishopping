from rest_framework.viewsets import ModelViewSet

from apps.rp.models import Rp
from apps.rp.api.serializers import RpSerializer


class RpViewSet(ModelViewSet):
    queryset = Rp.objects.all()
    serializer_class = RpSerializer
