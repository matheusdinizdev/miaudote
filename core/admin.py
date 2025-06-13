from django.contrib import admin
from .models import CustomUser, PessoaFisica, ONG, Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'porte', 'idade', 'usuario', 'contato_whatsapp')
    list_filter = ('tipo', 'porte', 'idade')

@admin.register(CustomUser)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo_usuario')
    list_filter = ('tipo_usuario',)

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cpf')

@admin.register(ONG)
class ONGAdmin(admin.ModelAdmin):
    list_display = ('nome_ong', 'responsavel', 'cnpj')
