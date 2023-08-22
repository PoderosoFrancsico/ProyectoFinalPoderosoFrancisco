from django.urls import path
from pagina import views

urlpatterns = [
    path('', views.inicio, name='inicio.html'),
    path('blogs', views.crearblog, name='blogs.html'),
    path('about', views.about, name='about.html'),
    path('editarperfil', views.editar_perfil, name='editarperfil.html'),
    path('avatar', views.changeavatar, name='avatar.html'),
    path('leerblogs', views.leerblogs, name='leerblogs.html'),
    path('borrarblogs/<blog_titulo>/', views.borrarblogs, name='borrarblogs'),
    path('editarblog/<blog_titulo>/', views.editarblog, name='editarblog'),
]