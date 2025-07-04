from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import CustomUser , PessoaFisica, ONG, Animal
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None
        if user is not None and user.check_password(senha):
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email ou senha incorretos.')
    return render(request, 'core/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        cpf = request.POST.get('cpf')

        nome_ong = request.POST.get('nome_ong')
        cnpj = request.POST.get('cnpj')
        responsavel = request.POST.get('responsavel')

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'core/cadastro.html')

        try:
            usuario = CustomUser.objects.create_user(
                username=nome,
                email=email,
                password=senha,
                tipo_usuario=tipo_usuario
            )
            if tipo_usuario == 'PESSOA':
                if cpf:
                    PessoaFisica.objects.create(usuario=usuario, cpf=cpf)
                else:
                    messages.error(request, 'CPF obrigatório para Pessoa Física.')
                    return render(request, 'core/cadastro.html')
            else:
                if nome_ong and cnpj and responsavel:
                    ONG.objects.create(usuario=usuario, nome_ong=nome_ong, cnpj=cnpj, responsavel=responsavel)
                else:
                    messages.error(request, 'Campos obrigatórios para ONG não preenchidos.')
                    return render(request, 'core/cadastro.html')

            messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Erro no cadastro: {str(e)}')
            return render(request, 'core/cadastro.html')

    return render(request, 'core/cadastro.html')

from django.shortcuts import render
from .models import Animal

def home_view(request):
    tipo = request.GET.get('tipo')
    porte = request.GET.get('porte')
    idade_min = request.GET.get('idade_min')
    idade_max = request.GET.get('idade_max')

    animais = Animal.objects.all().order_by('-id')

    if tipo:
        animais = animais.filter(tipo=tipo)
    if porte:
        animais = animais.filter(porte=porte)
    if idade_min:
        animais = animais.filter(idade__gte=idade_min)
    if idade_max:
        animais = animais.filter(idade__lte=idade_max)

    return render(request, 'core/home.html', {'animais': animais})


def logout_view(request):
    logout(request)
    return redirect('login')

def sobre_view(request):
    return render(request, 'core/sobre.html')

@login_required
def cadastrar_animal_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        porte = request.POST.get('porte')
        idade = request.POST.get('idade')
        descricao = request.POST.get('descricao')
        contato_whatsapp = request.POST.get('contato_whatsapp')
        contato_email = request.POST.get('contato_email')
        foto = request.FILES.get('foto')

        if not (nome and tipo and porte and idade and descricao and contato_whatsapp and contato_email):
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
            return redirect('cadastrar_animal')
        
        Animal.objects.create(
            nome=nome,
            tipo=tipo,
            porte=porte,
            idade=idade,
            descricao=descricao,
            contato_whatsapp=contato_whatsapp,
            contato_email=contato_email,
            foto=foto,
            usuario=request.user
        )
        messages.success(request, 'Animal cadastrado com sucesso!')
        return redirect('home')
    return render(request, 'core/cadastrar_animal.html')

@login_required
def excluir_animal_view(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if animal.usuario != request.user:
        return HttpResponseForbidden("Você não tem permissão para excluir esse animal.")
    if request.method == "POST":
        animal.delete()
        messages.success(request, "Animal excluído com sucesso!")
        return redirect('home')
    return redirect('home')