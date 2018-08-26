from django.db import models

from apps.colaborador.models import Colaborador
from apps.contacontabil.models import ContaContabil
from apps.empresa.models import Empresa
from apps.fornecedor.models import Fornecedor
from apps.rateio.models import Rateio
from apps.retencoes.models import Retencoes


class Rp(models.Model):
    rp = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    conta_contabil = models.ForeignKey(ContaContabil, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    forma_pagamento = models.CharField(max_length=50)
    valor_nfe = models.FloatField()
    retencoes = models.ManyToManyField(to=Retencoes)
    rateio = models.ManyToManyField(to=Rateio)
    detalhe_pagamento = models.TextField()
    data_pagamento = models.DateField()
    numero_nfe = models.IntegerField()
    aprovada = models.BooleanField(default=False)
    arquivo_nfe = models.FileField(upload_to='arquivos_nfe', blank=True, null=True)
    arquivo_boleto = models.FileField(upload_to='arquivos_boleto', blank=True, null=True)
