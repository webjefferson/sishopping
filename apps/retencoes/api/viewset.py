from rest_framework.viewsets import ModelViewSet

from apps.retencoes.models import Retencoes
from apps.retencoes.api.serializers import RetencoesSerializer


class RetencoesViewSet(ModelViewSet):
    queryset = Retencoes.objects.all()
    serializer_class = RetencoesSerializer
