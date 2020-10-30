from django.db import models

# Create your models here.
class informacoes_pescaria(models.Model):
    dia = models.DateField(blank=False, null=False)
    hora_pesca = models.TimeField(blank=False, null=False)
    acompanhantes = models.CharField(max_length = 100, blank=False, null = False, help_text="Insira os acompanhantes")
    local_pesca = models.CharField(max_length = 150, blank=False, null=False, help_text="Insira a localização")

    def __str__(self):
        return self.local_pesca