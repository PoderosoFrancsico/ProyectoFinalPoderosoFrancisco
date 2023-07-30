from django.urls import path
from pagina import views

urlpatterns = [
    path('', views.inicio, name='inicio.html'),
    path('blogs', views.blogs, name='blogs.html'),
    path('about', views.about, name='about.html'),
    path('singin', views.usuarios, name='singin.html'),
    
]