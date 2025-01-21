from django import forms 
from .models import Usuario, UserLoginInfo

class UsuarioForm(forms.ModelForm): 
    class Meta: 
        model = Usuario 
        fields = ['email', 'senha']
        
class UserLoginInfoForm(forms.ModelForm):
    class Meta: 
        model = UserLoginInfo 
        fields = ['user']