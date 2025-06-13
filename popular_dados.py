# python manage.py shell < popular_dados.py
# Precisa ser alterado, houve mudanças no modelo de dados

from core.models import Usuario, PessoaFisica, ONG, Animal
import random

# Limpa os dados existentes
Usuario.objects.all().delete()
PessoaFisica.objects.all().delete()
ONG.objects.all().delete()
Animal.objects.all().delete()

# Listas para gerar dados
nomes = ["Carlos", "Fernanda", "João", "Mariana", "Pedro", "Ana", "Lucas", "Juliana", "Gabriel", "Laura"]
emails = [f"{nome.lower()}@email.com" for nome in nomes]
cpfs = [f"{i:011d}" for i in range(10000000000, 10000000010)]
cnpjs = [f"{i:014d}" for i in range(12345678000100, 12345678000110)]
tipos_animais = ['Cachorro', 'Gato', 'Outro']
portes = ['Pequeno', 'Médio', 'Grande']
especies_outros = ['Coelho', 'Papagaio', 'Hamster', 'Porquinho-da-índia']

usuarios = []

# Cria 5 usuários Pessoa Física
for i in range(5):
    user = Usuario.objects.create(
        nome=nomes[i],
        email=emails[i],
        senha='senha123',
        tipo_usuario='PESSOA'
    )
    PessoaFisica.objects.create(usuario=user, cpf=cpfs[i])
    usuarios.append(user)

# Cria 5 usuários ONG
for i in range(5, 10):
    user = Usuario.objects.create(
        nome=nomes[i],
        email=emails[i],
        senha='senha123',
        tipo_usuario='ONG'
    )
    ONG.objects.create(usuario=user, nome_ong=f"ONG {nomes[i]}", cnpj=cnpjs[i-5], responsavel=nomes[i])
    usuarios.append(user)

# Cria 10 animais
for i in range(10):
    tipo = random.choice(tipos_animais)
    nome_animal = f"{tipo} #{i+1}"
    if tipo == 'Outro':
        nome_animal = random.choice(especies_outros)
    Animal.objects.create(
        nome=nome_animal,
        tipo=tipo,
        porte=random.choice(portes),
        idade=random.randint(1, 10),
        descricao=f"{nome_animal} muito amigável e saudável.",
        contato_whatsapp=f"(35) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
        contato_email=usuarios[i % 10].email,
        foto_url="https://placekitten.com/200/300",
        usuario=usuarios[i % 10]
    )

print("✅ Dados fictícios criados com sucesso!")
