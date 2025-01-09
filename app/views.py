from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .models import UserLoginInfo
from .forms import UsuarioForm

def login(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Email ou senha incorretos')
    else:
        form = UsuarioForm()
    return render(request, 'login.html', {'form': form})


def index(request): 
    return render(request, 'index.html')

@login_required 
def usuarios_login(request): 
    users = UserLoginInfo.objects.all() 
    return render(request, 'usuarios_login.html', {'users': users})

def registrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecionar para a página de login após o registro
    else:
        form = UsuarioForm()
    return render(request, 'registrar.html', {'form': form})