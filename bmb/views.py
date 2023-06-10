from django.shortcuts import render,redirect
from .models import *
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def completo(request):
    return render(request, "completo.html")

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