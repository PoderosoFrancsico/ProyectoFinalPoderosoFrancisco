from django.urls import path, include
from login import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_request, name='login'),
    path('singin', views.register, name='singin'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout')    
]