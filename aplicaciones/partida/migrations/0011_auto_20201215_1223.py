# Generated by Django 3.1.4 on 2020-12-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0010_auto_20201215_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
    ]