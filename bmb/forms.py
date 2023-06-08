from django import forms
from django.contrib.auth.forms import UserCreationForm
from bmb.models import Usuario

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']