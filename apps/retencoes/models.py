from django.db import models

acrescimo = '1'
desconto = '2'
imposto_mun = '3'
imposto_est = '4'
imposto_fed = '5'

TIPORETENCAO = [
    (acrescimo, 'Acrescimo'),
    (desconto, 'Desconto'),
    (imposto_mun, 'Imposto Municipal'),
    (imposto_est, 'Imposto Estadual'),
    (imposto_fed, 'Imposto Federal'),
]


class Retencoes(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=30, choices=TIPORETENCAO)
    percentual = models.FloatField()
    valor = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nome + " - " + self.percentual.__str__() + "%"
