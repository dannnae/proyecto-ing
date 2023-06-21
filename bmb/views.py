from django.shortcuts import render,redirect
from .models import *
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index') #redirigir al login
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def exit(request):
    logout(request)
    return redirect('index')

def arriendos(request):
    return render(request, "arriendos.html")

def reparaciones(request):
    return render(request, "reparaciones.html")

def accesorios(request):
    return render(request, "accesorios.html")

def nosotros(request):
    return render(request, "nosotros.html")

def formarriendo(request):
    return render(request, "form-arriendo.html")