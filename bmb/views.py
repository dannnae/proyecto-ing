from django.shortcuts import render,redirect
from .models import *
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    user = request.user
    return render(request, "index.html", {'user': user})



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index') #redirigir al login
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['user_logged_in'] = True
            return redirect('index') 
        
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('index') 



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