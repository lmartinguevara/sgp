# Generated by Django 3.1.4 on 2020-12-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0007_partida_concepto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='concepto',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
