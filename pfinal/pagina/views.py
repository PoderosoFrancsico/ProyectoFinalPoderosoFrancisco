from django.shortcuts import render
from django.http import HttpResponse
from pagina.models import *
from pagina.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
#from django.views.generic.detail import DetailView from django.views.generic.detail.edit import CreateView, Update view, DeleteView

# Create your views here.



def inicio(request):
    
    return render(request, 'inicio.html')



#def inicio(request):
 #   avatares = Avatar.objects.filter(user=request.user.id)
  #  return render(request, 'inicio.html', {'url':avatares[0].imagen.url})
    
@login_required
def blogs(request):
    return render(request, 'blogs.html')

def about(request):
    return render(request, 'about.html')
    

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario =UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']

            usuario.save()
            return render(request, 'inicio.html')

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, 'editarperfil.html', {'miFormulario': miFormulario, 'usuario': usuario})

def changeavatar(request):

    if request.method == 'POST':
        
        miFormulario= AvatarForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)

            avatar= Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])

            avatar.save()

            return render(request, 'inicio.html')
        
    else:
        miFormulario= AvatarForm()
    return render(request, 'avatar.html', {'miFormulario':miFormulario})

def leerblogs(request):

    lblogs = Blogs.objects.all()

    contexto = {'lblogs': lblogs}

    return render(request, 'leerblogs.html', contexto)


def crearblog(request):

    if request.method == 'POST':
        miFormulario = NuevoBlog(request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            blog = Blogs        (titulo=informacion['titulo'], 
                                          cuerpo=informacion['cuerpo'], 
                                          imagen=informacion['imagen'])
            blog.save()
            return render(request, 'inicio.html')
    else: 
        miFormulario= NuevoBlog()

    return render(request, 'blogs.html', {'miFormulario': miFormulario})