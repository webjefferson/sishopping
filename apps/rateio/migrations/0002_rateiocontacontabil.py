# Generated by Django 2.1 on 2018-08-26 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacontabil', '0001_initial'),
        ('rateio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateioContaContabil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta_contabil', models.ManyToManyField(to='contacontabil.ContaContabil')),
                ('rateio', models.ManyToManyField(to='rateio.Rateio')),
            ],
        ),
    ]