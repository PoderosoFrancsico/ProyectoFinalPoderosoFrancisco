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
    path('blogs/list', views.BlogsList.as_view(), name='list'),
    path(r'^(?P<pk>/d+)$', views.BlogsDetalle.as_view(), name='detail'),
    path(r'^nuevo$', views.BlogsCreate.as_view(), name='new'),
    path(r'^editar(?P<pk>/d+)$', views.BlogsUpdate.as_view(), name='edit'),
    path(r'^borrar(?P<pk>/d+)$', views.BlogsDelete.as_view(), name='delete'),

]