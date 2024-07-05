from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alumno, Genero, Compra
from .forms import ContactForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, RegistroForm, CompraForm

def index(request):
    context = {}
    return render(request, 'cripto/index.html', context)

def criptoactivos(request):
    return render(request, 'cripto/criptoactivos.html')

@login_required
def comprar(request):
    return render(request, 'cripto/comprar.html')

def vender(request):
    return render(request, 'cripto/vender.html')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirige a la página de inicio si el usuario ya está logueado
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. Bienvenido(a) a la plataforma!")
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'cripto/registro.html', {'form': form})

def nosotros(request):
    return render(request, 'cripto/nosotros.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado exitosamente.')
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'cripto/contacto.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('index')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'cripto/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('index')

def listadoSQL(request):
    cripto = Alumno.objects.raw('SELECT * FROM cripto_alumno')
    context = {"cripto": cripto}
    return render(request, 'cripto/listadoSQL.html', context)

def exit (request):
    logout(request)
    return redirect('index')

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido(a) a la plataforma!')
            return redirect('index')
    else:
        form = RegistroForm()
    return render(request, 'cripto/registro.html', {'form': form})

@login_required
def comprar(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        run = request.POST['run']
        cryptocurrency = request.POST['cryptocurrency']
        local_currency_amount = request.POST['local-currency-amount']
        crypto_amount = request.POST['crypto-amount']
        
        compra = Compra(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            run=run,
            cryptocurrency=cryptocurrency,
            local_currency_amount=local_currency_amount,
            crypto_amount=crypto_amount
        )
        compra.save()
        
        messages.success(request, 'Compra realizada exitosamente')
        return redirect('mis_compras')
    
    return render(request, 'cripto/comprar.html')


@login_required
def mis_compras(request):
    compras = Compra.objects.filter(user=request.user)
    return render(request, 'cripto/mis_compras.html', {'compras': compras})