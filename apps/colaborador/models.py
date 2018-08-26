from django.db import models
from apps.setor.models import Setor


class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
