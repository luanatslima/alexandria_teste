from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Adicione campos adicionais se necessário

    def __str__(self):
        return self.username

class Usuario(models.Model): 
    email = models.EmailField(unique=True) 
    senha = models.CharField(max_length=30) 
    
    def __str__(self): 
        return self.email
    
class UserLoginInfo(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    last_login = models.DateTimeField(auto_now=True)