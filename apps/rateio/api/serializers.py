from rest_framework.serializers import ModelSerializer

from apps.rateio.models import Rateio


class RateioSerializer(ModelSerializer):
    class Meta:
        model = Rateio
        fields = ('id', 'conta_contabil', 'valor',)
