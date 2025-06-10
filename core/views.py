from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Usando username para autenticar, por padrão
        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '🐾 Miau! Parece que o e-mail ou a senha estão incorretos. Confira e tente novamente para ajudar nossos amiguinhos a encontrar um lar!')
    
    return render(request, 'core/login.html')

@login_required
def home_view(request):
    return render(request, 'core/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
