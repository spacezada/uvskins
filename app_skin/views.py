from django.shortcuts import render
from .models import Skin, Usuario


# Create your views here.

def home(request):
    return render(request,'pags/login.html')


def login(request):
    return render(request,'pags/login.html')

def skin(request):
    skins = Skin.objects.all()
    return render(request, 'pags/skin.html', {'skins': skins})

def cadastro(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.nome = request.POST.get('email')
    novo_usuario.nome = request.POST.get('senha')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all
    }
    
    return render(request,'pags/cadastro.html', usuarios)


