from rest_framework.viewsets import ModelViewSet

from apps.orcamento.api.serializers import OrcamentoSerializer
from apps.orcamento.models import Orcamento


class OrcamentoViewSet(ModelViewSet):
    queryset = Orcamento.objects.all()
    serializer_class = OrcamentoSerializer