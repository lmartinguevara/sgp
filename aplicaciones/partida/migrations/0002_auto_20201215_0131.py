# Generated by Django 3.1.4 on 2020-12-15 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partida.partida'),
        ),
    ]
