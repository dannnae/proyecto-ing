from django import forms
from django.contrib.auth.forms import UserCreationForm
from bmb.models import Usuario, Solicitud

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
    class Meta:
        model = Solicitud
        fields = ['tipo_soli', 'descripcion', 'fecha_inicio',  'metodo_pago']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email']







# class SolicitudForm(forms.ModelForm):
#     fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))


#     class Meta:
#         model = Solicitud
#         fields = ['usuario', 'descripcion', 'fecha_inicio', 'metodo_pago']
#         widgets = {
#             'metodo_pago': forms.Select(attrs={'class': 'form-label'}),
#             'usuario': forms.HiddenInput(),
#         }