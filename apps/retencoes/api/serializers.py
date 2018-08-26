from rest_framework.serializers import ModelSerializer

from apps.retencoes.models import Retencoes


class RetencoesSerializer(ModelSerializer):
    class Meta:
        model = Retencoes
        fields = ('id', 'nome', 'tipo', 'percentual', 'valor',)
