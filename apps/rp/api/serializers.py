from rest_framework.serializers import ModelSerializer

from apps.rp.models import Rp


class RpSerializer(ModelSerializer):
    class Meta:
        model = Rp
        fields = ['rp', 'empresa', 'conta_contabil', 'colaborador', 'fornecedor', 'forma_pagamento', 'valor_nfe',
                      'retencoes', 'rateio', 'detalhe_pagamento', 'data_pagamento', 'numero_nfe']
