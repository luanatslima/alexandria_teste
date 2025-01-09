from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

class Usuario(models.Model): 
    email = models.EmailField(unique=True) 
    senha = models.CharField(max_length=30) 
    
    def __str__(self): 
        return self.email
    
class UserLoginInfo(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    last_login = models.DateTimeField(auto_now=True)

@receiver(user_logged_in)
def update_user_login_info(sender, request, user, **kwargs):
    UserLoginInfo.objects.update_or_create(user=user, defaults={'last_login': timezone.now()})
