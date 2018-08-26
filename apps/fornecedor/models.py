from django.db import models

from apps.banco.models import Banco
from apps.endereco.models import Endereco


class Telefone(models.Model):
    ddd = models.IntegerField()
    numero = models.IntegerField()

    def __str__(self):
        return "(" + self.ddd.__str__() + ") " + self.numero.__str__()


class Fornecedor(models.Model):
    codigo_jde = models.IntegerField()
    cnpj = models.IntegerField()
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    insc_estad = models.IntegerField()
    insc_mun = models.IntegerField(blank=True, null=True)
    data_situacao_cadastral = models.DateField()
    cnae = models.IntegerField()
    optante_simples = models.BooleanField()
    descricao_servicos_prestados = models.TextField()
    contato_empresa = models.CharField(max_length=50)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.cnpj.__str__() + " - " + self.razao_social
