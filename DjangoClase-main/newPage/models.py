from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.

""" 

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
        return str(self.nombre)+" "+str(self.apellido) """
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not correo:
            raise ValueError('El correo electrónico debe ser proporcionado')

        usuario = self.model(correo=correo, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(correo, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    Nom = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    fechaNacimiento = models.DateField(blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100, primary_key=True)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField()

    # Campos requeridos para el modelo de usuario personalizado
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Relación con los grupos
    groups = models.ManyToManyField(Group, related_name='usuarios')

    # Relación con los permisos de usuario
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')

    USERNAME_FIELD = 'correo'

    objects = UsuarioManager()

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido)


""" 
class CustomUser(AbstractUser):
    # Campos personalizados adicionales
    username= models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField() """