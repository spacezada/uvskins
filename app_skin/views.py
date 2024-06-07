from django.shortcuts import render
from .models import Skin, Usuario
from django.shortcuts import render, get_object_or_404
from .models import Skin

# Create your views here.

from django.shortcuts import render
from .models import Skin

def login(request):
    return render(request, 'pags/login.html')

def home(request):
    skins = Skin.objects.all()
    return render(request, 'pags/home.html', {'skins': skins})

def cadastro(request):
    return render(request, 'pags/cadastro.html')

def skin(request, skin_id):
    skin = get_object_or_404(Skin, pk=skin_id)
    return render(request, 'pags/skin.html', {'skin': skin})