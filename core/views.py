from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import CustomUser , PessoaFisica, ONG, Animal

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

def home_view(request):
    return render(request, 'core/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
