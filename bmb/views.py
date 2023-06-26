from datetime import date
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render,redirect
from .models import *
from datetime import datetime, timedelta
from .forms import RegistrationForm, SolicitudForm, SolicitudForm2, UsuarioForm
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




#ARRIENDO


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






def reparaciones(request):
    SolicitudUsuarioFormSet = modelformset_factory(
        Solicitud, 
        form=SolicitudForm2, 
        extra=1,
        can_delete=False
    )
    
    if request.method == 'POST':
        formset = SolicitudUsuarioFormSet(request.POST, prefix='solicitud')
        if formset.is_valid():
            for form in formset:
                solicitud = form.save(commit=False)
                solicitud.usuario = Usuario.objects.get(id=request.user.id)
                solicitud.save()
                
                despacho = Despacho.objects.create(
                    estado='Por confirmar',
                    fecha_estimada=datetime.now().date() + timedelta(days=5)  # Calcular la fecha estimada dentro de 5 días
                )
                
                bici_reparacion = BiciReparacion.objects.create(
                    modelo='modelo',
                    comentarios='comentarios',
                    marca='marca',
                    solicitud=solicitud,
                    despacho=despacho
                )
                # Realizar otras operaciones relacionadas con la bicicleta si es necesario
                
            return redirect('index')
    else:
        formset = SolicitudUsuarioFormSet(queryset=Solicitud.objects.none(), prefix='solicitud')
    
    return render(request, 'reparaciones.html', {'formset': formset})



#CRUD


def ver_solicitudes(request):
    nombre = request.GET.get('nombre')  # Obtener el valor del parámetro 'nombre' de la solicitud GET

    if nombre is None:
        solicitudes = Solicitud.objects.all()
    else:
        solicitudes = Solicitud.objects.filter(tipo_soli__nombre=nombre)

    return render(request, 'ver_solicitudes.html', {'solicitudes': solicitudes})




def modificar_solicitud(request, pk):
    solicitud = Solicitud.objects.get(pk=pk)
    pk = request.GET.get('pk')
    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud, )
        if form.is_valid():
            form.save()
            return redirect('listar_solicitudes')
    else:
        form = SolicitudForm(instance=solicitud)
    return render(request, 'modificar_solicitud.html', {'form': form})



def eliminar_solicitud(request, pk):
    solicitud = Solicitud.objects.get(pk=pk)
    solicitud.delete()
    return redirect('listar_solicitudes')


def exit(request):
    logout(request)
    return redirect('index')


def arriendos(request):
    bicicletas = Bicicleta.objects.all()
    usuarios = Usuario.objects.all()
    context = {
        'bicicletas': bicicletas,
        'usuarios': usuarios
    }
    return render(request, 'arriendos.html', context)


def accesorios(request):
    return render(request, "accesorios.html")

def nosotros(request):
    return render(request, "nosotros.html")
