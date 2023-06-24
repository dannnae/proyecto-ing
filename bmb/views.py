from datetime import date
from django.forms import modelformset_factory
from django.shortcuts import render,redirect
from .models import *
from .forms import RegistrationForm, SolicitudForm, UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout




def index(request):
    user = request.user
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'user': user, 'usuarios': usuarios})




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
    usuarios = Usuario.objects.all()
    return render(request, 'arriendos.html', {'usuarios': usuarios})

def reparaciones(request):
    return render(request, "reparaciones.html")

def accesorios(request):
    return render(request, "accesorios.html")

def nosotros(request):
    return render(request, "nosotros.html")







#agregar usuario


def formarriendo(request):
    SolicitudUsuarioFormSet = modelformset_factory(
        Solicitud, 
        form=SolicitudForm, 
        extra=1,
        can_delete=False  # Si no deseas permitir eliminar solicitudes del formset
    )
    
    if request.method == 'POST':
        formset = SolicitudUsuarioFormSet(request.POST, prefix='solicitud')
        if formset.is_valid():
            for form in formset:
                solicitud = form.save(commit=False)
                solicitud.usuario = Usuario.objects.get(id=request.user.id)
                solicitud.save()
            return redirect('index')
    else:
        formset = SolicitudUsuarioFormSet(queryset=Solicitud.objects.none(), prefix='solicitud')
    
    return render(request, 'formarriendo.html', {'formset': formset})



def listar_solicitudes(request):
    usuario_actual = request.user
    solicitudes = Solicitud.objects.filter(usuario=usuario_actual)
    return render(request, 'listar_solicitudes.html', {'solicitudes': solicitudes})






