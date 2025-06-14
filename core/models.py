from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    TIPOS = (
        ('PESSOA', 'Pessoa Física'),
        ('ONG', 'ONG'),
    )
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS, blank=True)

    def __str__(self):
        return self.username or self.email or str(self.pk)


class PessoaFisica(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"{self.usuario.username} (CPF: {self.cpf})"


class ONG(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nome_ong = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_ong} - Resp: {self.responsavel}"


class Animal(models.Model):
    TIPOS = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Outro', 'Outro'),
    )
    PORTES = (
        ('Pequeno', 'Pequeno'),
        ('Médio', 'Médio'),
        ('Grande', 'Grande'),
    )

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    porte = models.CharField(max_length=20, choices=PORTES)
    idade = models.IntegerField()
    descricao = models.TextField()
    contato_whatsapp = models.CharField(max_length=20)
    contato_email = models.EmailField()
    foto = models.ImageField(upload_to='fotos_pets/', blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"

