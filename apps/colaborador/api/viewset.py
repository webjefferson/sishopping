from rest_framework.viewsets import ModelViewSet

from apps.colaborador.models import Colaborador
from apps.colaborador.api.serializers import ColaboradorSerializer


class ColaboradorViewSet(ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
