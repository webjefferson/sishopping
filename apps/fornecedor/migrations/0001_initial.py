# Generated by Django 2.1 on 2018-08-26 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banco', '0001_initial'),
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_jde', models.IntegerField()),
                ('cnpj', models.IntegerField()),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(blank=True, max_length=100, null=True)),
                ('insc_estad', models.IntegerField()),
                ('insc_mun', models.IntegerField(blank=True, null=True)),
                ('data_situacao_cadastral', models.DateField()),
                ('cnae', models.IntegerField()),
                ('optante_simples', models.BooleanField()),
                ('descricao_servicos_prestados', models.TextField()),
                ('contato_empresa', models.CharField(max_length=50)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.Banco')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.IntegerField(max_length=3)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='telefone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.Telefone'),
        ),
    ]
