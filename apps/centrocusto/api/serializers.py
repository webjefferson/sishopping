from rest_framework.serializers import ModelSerializer

from apps.centrocusto.models import CentroCusto


class CentroCustoSerializer(ModelSerializer):
    class Meta:
        model = CentroCusto
        fields = ('id', 'centro_custo', 'descricao', 'empresa',)
