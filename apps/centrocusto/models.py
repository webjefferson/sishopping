from django.db import models

from apps.empresa.models import Empresa


class CentroCusto(models.Model):
    centro_custo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.centro_custo
