from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.

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


        return self.create_user(correo, password, **extra_fields)
    
    def get_by_natural_key(self, rut):
        return self.get(rut=rut)



class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100, primary_key=True)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    activo = models.IntegerField()
    fechaNacimiento = models.DateField(null=True, blank=True)

    # Campos requeridos para el modelo de usuario personalizado
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Relación con los grupos
    groups = models.ManyToManyField(Group, related_name='usuarios')

    # Relación con los permisos de usuario
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')
    activo = models.IntegerField(blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    USERNAME_FIELD = 'correo'

    objects = UsuarioManager()

    def __str__(self):
        return str(self.username) + " " + str(self.apellido)


