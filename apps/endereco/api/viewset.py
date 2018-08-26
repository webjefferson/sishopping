from rest_framework.viewsets import ModelViewSet

from apps.endereco.models import Endereco
from apps.endereco.api.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
