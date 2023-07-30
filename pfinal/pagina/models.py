from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellio: {self.apellido} - Email: {self.email}'
        