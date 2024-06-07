from django.urls import path
from . import views

app_name = 'skins'

urlpatterns = [
    path('', views.home, name='home'),        # Página inicial do aplicativo
    path('skin/', views.skin, name='skin'),   # Página específica para 'skin'
    path('login/', views.login, name='login'), 
    path('cadastro/', views.cadastro, name='cadastro'),
    ]