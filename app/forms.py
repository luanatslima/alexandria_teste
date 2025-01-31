from django import forms 
from .models import Usuario, UserLoginInfo
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import get_user_model

class UsuarioForm(forms.ModelForm): 
    class Meta: 
        model = Usuario 
        fields = ['email', 'senha']
        
class UserLoginInfoForm(forms.ModelForm):
    class Meta: 
        model = UserLoginInfo 
        fields = ['user']

class CadastroForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

User = get_user_model()  # Isso evita importação direta do modelo

class CadastroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')