from django.db import models

# Create your models here.
class cadastro_usuario(models.Model):
    nome_usuario = models.CharField(max_length=50, blank=False, null=False, help_text="Insira o nome do usuario")
    cpf = models.FloatField(max_length=20,blank=False,null=False, help_text="Insira o CPF")
    telefone = models.IntegerField(blank=False,null=False, help_text="Insira o telefone")
    endereco = models.CharField(max_length=80, blank=False, null=False, help_text="Insira o endereco")
    foto_de_perfil = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome_usuario

class Meta:
    verbose_name = "Usuários"