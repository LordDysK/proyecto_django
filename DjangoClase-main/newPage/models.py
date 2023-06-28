from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Usuario(models.Model):
    # Nombre Usuario - Nombre - Apellido- fecha Nacimiento
    # correo - telefono - activo
    Nom = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100, primary_key=True)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)


""" 
class CustomUser(AbstractUser):
    # Campos personalizados adicionales
    username= models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField() """