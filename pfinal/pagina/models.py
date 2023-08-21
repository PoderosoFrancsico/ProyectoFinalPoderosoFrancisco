from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellio: {self.apellido} - Email: {self.email}'
    

class Blogs(models.Model):

    titulo=models.CharField(max_length=60)
    cuerpo=models.CharField(max_length=1200)
    imagen = models.ImageField(upload_to='portada', null=True, blank=True)

    def __str__(self):
        return f'Titulo: {self.titulo}'
        

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self) -> str:
            
        
        return f'Nombre: {self.user} - {self.imagen }' 
    