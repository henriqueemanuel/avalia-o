from django.db import models

# Create your models here.

class informacoes_peixe(models.Model):
    nome_peixe = models.CharField(max_length=20, blank=False, null=False, help_text="Dê um nome ao peixe")
    massa = models.FloatField(blank=False, null=False, help_text="Insira a massa em KG")
    tamanho = models.IntegerField(blank=False, null=False, help_text="Insira o tamanho em CM")
    imagem_peixe = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_peixe