from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .models import UserLoginInfo
from .forms import UsuarioForm
from .forms import CadastroForm

def login(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            return redirect('index')
    else:
        form = UsuarioForm()
    return render(request, 'login.html', {'form': form})


def index(request): 
    return render(request, 'index.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

@login_required 
def usuarios_login(request): 
    users = UserLoginInfo.objects.all() 
    return render(request, 'usuarios_login.html', {'users': users})


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})