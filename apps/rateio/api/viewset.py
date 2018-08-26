from rest_framework.viewsets import ModelViewSet

from apps.rateio.models import Rateio
from apps.rateio.api.serializers import RateioSerializer


class RateioViewSet(ModelViewSet):
    queryset = Rateio.objects.all()
    serializer_class = RateioSerializer
