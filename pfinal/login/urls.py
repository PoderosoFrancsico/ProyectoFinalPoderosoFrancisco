from django.urls import path, include
from login import views

urlpatterns = [
    path('', views.login_request, name='login'),
    path('singin', views.register, name='singin'),
    
]