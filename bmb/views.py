from django.shortcuts import render,redirect
from .models import *
from .forms import RegistrationForm


def login(request):
    return render(request, "login.html")

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










