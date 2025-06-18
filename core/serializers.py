from rest_framework import serializers
from .models import Animal, PessoaFisica, ONG, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'tipo_usuario']

class PessoaFisicaSerializer(serializers.ModelSerializer):
    usuario = CustomUserSerializer()

    class Meta:
        model = PessoaFisica
        fields = ['id', 'usuario', 'cpf']

class ONGSerializer(serializers.ModelSerializer):
    usuario = CustomUserSerializer()

    class Meta:
        model = ONG
        fields = ['id', 'usuario', 'nome_ong', 'cnpj', 'responsavel']

class AnimalSerializer(serializers.ModelSerializer):
    usuario = CustomUserSerializer()

    class Meta:
        model = Animal
        fields = '__all__'
