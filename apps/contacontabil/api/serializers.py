from rest_framework.serializers import ModelSerializer

from apps.contacontabil.models import ContaContabil


class ContaContabilSerializer(ModelSerializer):
    class Meta:
        model = ContaContabil
        fields = ('id', 'centro_custo', 'conta_analitica', 'conta_sintetica', 'descricao_conta',)
