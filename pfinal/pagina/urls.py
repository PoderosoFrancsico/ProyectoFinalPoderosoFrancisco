from django.urls import path
from pagina import views

urlpatterns = [
    path('', views.inicio, name='inicio.html'),
    
]