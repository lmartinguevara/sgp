# Generated by Django 3.1.4 on 2020-12-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0006_remove_partida_concepto'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='concepto',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
