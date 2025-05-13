from django.db import models

class Usuario(models.Model):
    TIPOS = (
        ('PESSOA', 'Pessoa Física'),
        ('ONG', 'ONG'),
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS)

    def __str__(self):
        return self.nome


class PessoaFisica(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"{self.usuario.nome} (CPF: {self.cpf})"


class ONG(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
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
    foto_url = models.URLField(blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
