# Generated by Django 3.1.4 on 2020-12-15 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0005_auto_20201215_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='concepto',
        ),
    ]
