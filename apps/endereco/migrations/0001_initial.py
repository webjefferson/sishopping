# Generated by Django 2.1 on 2018-08-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField()),
                ('estado', models.CharField(choices=[(1, 'AC'), (2, 'AL'), (3, 'AP'), (4, 'AM'), (5, 'BA'), (6, 'CE'), (7, 'DF'), (8, 'ES'), (9, 'GO'), (10, 'MA'), (11, 'MT'), (12, 'MS'), (13, 'MG'), (14, 'PA'), (15, 'PB'), (16, 'PR'), (17, 'PE'), (18, 'PI'), (19, 'RJ'), (20, 'RN'), (21, 'RS'), (22, 'RO'), (23, 'RR'), (24, 'SC'), (25, 'SP'), (26, 'SE'), (27, 'TO')], max_length=2)),
                ('cidade', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=30)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]