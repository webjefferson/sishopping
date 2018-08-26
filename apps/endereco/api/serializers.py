from rest_framework.serializers import ModelSerializer

from apps.endereco.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'cep', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento',)
