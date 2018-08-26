from django.db import models

Acre = 1
Alagoas = 2
Amapá = 3
Amazonas = 4
Bahia = 5
Ceará = 6
DistritoFederal = 7
EspíritoSanto = 8
Goiás = 9
Maranhão = 10
MatoGrosso = 11
MatoGrossodoSul = 12
MinasGerais = 13
Pará = 14
Paraíba = 15
Paraná = 16
Pernambuco = 17
Piauí = 18
RiodeJaneiro = 19
RioGrandedoNorte = 20
RioGrandedoSul = 21
Rondônia = 22
Roraima = 23
SantaCatarina = 24
SãoPaulo = 25
Sergipe = 26
Tocantins = 27

ESTADO = [
    (Acre, 'AC'),
    (Alagoas, 'AL'),
    (Amapá, 'AP'),
    (Amazonas, 'AM'),
    (Bahia, 'BA'),
    (Ceará, 'CE'),
    (DistritoFederal, 'DF'),
    (EspíritoSanto, 'ES'),
    (Goiás, 'GO'),
    (Maranhão, 'MA'),
    (MatoGrosso, 'MT'),
    (MatoGrossodoSul, 'MS'),
    (MinasGerais, 'MG'),
    (Pará, 'PA'),
    (Paraíba, 'PB'),
    (Paraná, 'PR'),
    (Pernambuco, 'PE'),
    (Piauí, 'PI'),
    (RiodeJaneiro, 'RJ'),
    (RioGrandedoNorte, 'RN'),
    (RioGrandedoSul, 'RS'),
    (Rondônia, 'RO'),
    (Roraima, 'RR'),
    (SantaCatarina, 'SC'),
    (SãoPaulo, 'SP'),
    (Sergipe, 'SE'),
    (Tocantins, 'TO'),
]
class Endereco(models.Model):
    cep = models.IntegerField()
    estado = models.CharField(max_length=2, choices=ESTADO)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    rua =models.CharField(max_length=50)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)