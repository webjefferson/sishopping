from rest_framework.viewsets import ModelViewSet

from apps.centrocusto.models import CentroCusto
from apps.centrocusto.api.serializers import CentroCustoSerializer


class CentroCustoViewSet(ModelViewSet):

    queryset = CentroCusto.objects.all()
    serializer_class = CentroCustoSerializer
