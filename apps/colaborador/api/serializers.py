from rest_framework.serializers import ModelSerializer

from apps.colaborador.models import Colaborador


class ColaboradorSerializer(ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ('id', 'nome', 'setor', 'username', 'senha', 'email',)
