from django.contrib import admin 
from .models import Usuario, UserLoginInfo

admin.site.register(Usuario)
admin.site.register(UserLoginInfo)