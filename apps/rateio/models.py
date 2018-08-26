from django.db import models

from apps.contacontabil.models import ContaContabil


class Rateio(models.Model):
    conta_contabil = models.ForeignKey(ContaContabil, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return self.conta_contabil.__str__() + " | R$" + self.valor.__str__()


class RateioContaContabil(models.Model):
    rateio = models.ManyToManyField(Rateio)
    conta_contabil = models.ManyToManyField(ContaContabil)
