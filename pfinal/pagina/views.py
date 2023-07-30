from django.shortcuts import render
from django.http import HttpResponse
from pagina.models import *
from pagina.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
#from django.views.generic.detail import DetailView from django.views.generic.detail.edit import CreateView, Update view, DeleteView

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

def blogs(request):
    return render(request, 'blogs.html')

def about(request):
    return render(request, 'about.html')
    
#def usuarios(request):

    if request.method == 'POST':
        miFormulario = UsuariosFormulario(request.POST)#aca llega la info del HTML
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'], 
                                          apellido=informacion['apellido'], 
                                          email=informacion['email'],)
            usuario.save()
            return render(request, 'inicio.html')
    else: 
        miFormulario= UsuariosFormulario()

    return render(request, r'singin.html', {'miFormulario': miFormulario})