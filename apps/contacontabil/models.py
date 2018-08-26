from django.db import models

from apps.centrocusto.models import CentroCusto


class ContaContabil(models.Model):
    centro_custo = models.ForeignKey(CentroCusto, on_delete=models.CASCADE)
    conta_analitica = models.CharField(max_length=20)
    conta_sintetica = models.CharField(max_length=5)
    descricao_conta = models.CharField(max_length=100)

    def __str__(self):
        return self.centro_custo.__str__() + " - " + self.conta_analitica + " - " + self.conta_sintetica + " - " + self.descricao_conta
