from django.urls import path, include
from pagina import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
]