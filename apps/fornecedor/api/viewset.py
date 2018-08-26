from rest_framework.viewsets import ModelViewSet

from apps.fornecedor.models import Fornecedor, Telefone
from apps.fornecedor.api.serializers import FornecedorSerializer, TelefoneSerializer


class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class TelefoneViewSet(ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer
