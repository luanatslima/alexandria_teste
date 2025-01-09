from django.urls import path
from .import views
from .views import usuarios_login

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index , name='index'),
    path('usuarios_login/', usuarios_login, name='usuarios_login'),
    path('registro/', views.registrar, name='registrar'),
]