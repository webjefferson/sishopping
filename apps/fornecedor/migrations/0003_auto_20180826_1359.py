# Generated by Django 2.1 on 2018-08-26 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0002_auto_20180826_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.Telefone'),
        ),
    ]
