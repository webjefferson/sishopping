from django.db import models

from apps.contacontabil.models import ContaContabil


class Orcamento(models.Model):
    conta_contabil = models.ForeignKey(ContaContabil, on_delete=models.CASCADE)
    data_inicial = models.DateField()
    data_final = models.DateField()
    valor_orc = models.FloatField()
    valor_realiz = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.conta_contabil.__str__() + self.valor_orc

class OrcamentoContaContabil(models.Model):
    orcamento = models.ManyToManyField(Orcamento)
    conta_contabil = models.ManyToManyField(ContaContabil)