# Generated by Django 2.1 on 2018-08-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retencoes', '0002_auto_20180826_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retencoes',
            name='tipo',
            field=models.CharField(choices=[(1, 'Acrescimo'), (2, 'Desconto'), (3, 'Imposto Municipal'), (4, 'Imposto Estadual'), (5, 'Imposto Federal')], max_length=30),
        ),
    ]
