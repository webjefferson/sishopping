from rest_framework.viewsets import ModelViewSet

from apps.banco.models import Banco
from apps.banco.api.serializers import BancoSerializer


class BancoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
