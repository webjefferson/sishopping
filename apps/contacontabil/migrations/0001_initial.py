# Generated by Django 2.1 on 2018-08-26 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centrocusto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaContabil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta_analitica', models.CharField(max_length=20)),
                ('conta_sintetica', models.CharField(max_length=5)),
                ('descricao_conta', models.CharField(max_length=100)),
                ('centro_custo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrocusto.CentroCusto')),
            ],
        ),
    ]