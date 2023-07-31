from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from login.form import *
# Create your views here.

def login_request(request):

    if request.method== 'POST':

        form= AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')

            user= authenticate(username=usuario, password=contras)

            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {'mensaje': f'Bienvenido {usuario} a este blog'})
            else:
                return render(request, 'inicio.html', {'mensaje': f'El usuario {usuario} no esta registrado'})
        else:
            return render(request, 'inicio.html', {'mensaje': f'Error en el formulario'})
    form=AuthenticationForm()

    return render(request, 'login.html', {'form':form})

def register(request):

    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html', {'mensaje': 'usuario creado'})
        
    else:
        #form=UserCreationForm()
        form=UserRegisterForm()

    return render(request, 'singin.html', {'form':form})