from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
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
                return render(request, 'inicio.html', {'menaje': f'Bienvenido {usuario} a este blog'})
            else:
                return render(request, 'inicio.html', {'menaje': f'El usuario {usuario} no esta registrado'})
        else:
            return render(request, 'inicio.html', {'menaje': f'Error en el formulario'})
    form=AuthenticationForm()

    return render(request, 'login.html', {'form':form})

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html', {'menaje': 'usuario creado'})
        
    else:
        form=UserCreationForm()
    return render(request, 'singin.html', {'form':form})