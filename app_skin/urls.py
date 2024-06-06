from django.urls import path
from . import views

app_name = 'skins'

urlpatterns = [
    path('skin/', views.skin, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('',views.home, name='home')
]