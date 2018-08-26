from django.db import models


class Banco(models.Model):
    nome = models.CharField(max_length=30)
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=15)
    operacao = models.CharField(max_length=5)
    dv = models.CharField(max_length=1)

    def __str__(self):
        return self.nome
