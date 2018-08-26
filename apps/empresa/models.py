from django.db import models

class Empresa(models.Model):
    entidade = models.CharField(max_length=10)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15)

    def __str__(self):
        return self.razao_social
