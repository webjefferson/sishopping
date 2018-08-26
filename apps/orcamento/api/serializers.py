from rest_framework.serializers import ModelSerializer

from apps.orcamento.models import Orcamento


class OrcamentoSerializer(ModelSerializer):
    class Meta:
        model = Orcamento
        fields = ['id', 'conta_contabil', 'data_inicial', 'data_final', 'valor_orc', 'valor_realiz', ]
