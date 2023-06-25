from django import forms
from django.contrib.auth.forms import UserCreationForm
from bmb.models import Usuario, Solicitud, Bicicleta

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }



class SolicitudForm(forms.ModelForm):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_soli'].widget = forms.HiddenInput()
        self.fields['tipo_soli'].initial = 1

    class Meta:
        model = Solicitud
        fields = ['tipo_soli', 'descripcion', 'fecha_inicio', 'metodo_pago']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']



class SolicitudForm2(forms.ModelForm):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_soli'].widget = forms.HiddenInput()
        self.fields['tipo_soli'].initial = 2


    class Meta:
        model = Solicitud
        fields = ['descripcion', 'fecha_inicio', 'metodo_pago', 'tipo_soli']
        widgets = {
            'tipo_soli': forms.HiddenInput(),
        }

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['nombre', 'descripcion', 'marca']



