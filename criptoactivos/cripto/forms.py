from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Compra

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'apellido', 'email', 'mensaje']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Primer nombre'}))
    last_name = forms.CharField(label='Apellido',max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Primer apellido'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': 'Correo electronico'}))
    
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        required=True,
        help_text='',  # Eliminar el mensaje de ayuda predeterminado
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})  # Opcional: añadir un placeholder
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['run', 'cryptocurrency', 'local_currency_amount', 'crypto_amount']
        widgets = {
            'crypto_amount': forms.TextInput(attrs={'readonly': 'readonly'}),
        }