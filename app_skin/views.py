from django.shortcuts import render
from .models import Skin
# Create your views here.

def login(request):
    return render(request,'pags/login.html')

def home(request):
    skins = Skin.objects.all()
    return render(request, 'pags/home.html', {'skins': skins})

def cadastro(request):
    return render(request,'pags/cadastro.html')



