from django.shortcuts import render, redirect
from .forms import UsuarioForm

def login(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            # Aqui você pode adicionar a lógica para autenticar o usuário
            # Por exemplo, verificar se o email e a senha estão corretos
            return redirect('logado')  # Redirecionar para uma página de sucesso
    else:
        form = UsuarioForm()
    return render(request, 'login.html', {'form': form})

def logado(request): 
    return render(request, 'logado.html')
