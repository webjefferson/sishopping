from rest_framework.viewsets import ModelViewSet

from apps.banco.models import Banco
from apps.banco.api.serializers import BancoSerializer


class BancoViewSet(ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
