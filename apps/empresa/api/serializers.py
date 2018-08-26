from rest_framework.serializers import ModelSerializer

from apps.empresa.models import Empresa


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 'entidade', 'razao_social', 'cnpj',)
