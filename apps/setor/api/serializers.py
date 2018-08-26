from rest_framework.serializers import ModelSerializer

from apps.setor.models import Setor


class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = ('id', 'nome',)
