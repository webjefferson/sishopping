from rest_framework.serializers import ModelSerializer

from apps.banco.models import Banco


class BancoSerializer(ModelSerializer):
    class Meta:
        model = Banco
        fields = ('id', 'nome', 'agencia', 'conta', 'operacao', 'dv',)
