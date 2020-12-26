from django.db import models

# Create your models here.

class Partida(models.Model):
    """Model definition for Partida."""

    # TODO: Define fields here
    TIPO_CHOICES = (
        ('0', 'INGRESO'),
        ('1', 'EGRESO'),
    )
    
    concepto = models.CharField('Concepto', max_length=50)
    nombre = models.CharField('Nombre', max_length=100)
    tipo = models.CharField('Tipo', max_length=50, choices=TIPO_CHOICES)
    partida_superior = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        """Meta definition for Partida."""

        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'

    def __str__(self):
        """Unicode representation of Partida."""
        return self.concepto + ' - ' + self.nombre