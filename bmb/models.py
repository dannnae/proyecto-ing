from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Solicitud(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    confirmacion = models.BooleanField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("El nombre de usuario debe ser especificado")
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener 'is_staff=True'")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener 'is_superuser=True'")

        return self._create_user(username, password, **extra_fields)


class Usuario(AbstractUser):
    es_cliente = models.BooleanField(null=True)
    es_tecnico = models.BooleanField(null=True)
    es_vendedor = models.BooleanField(null=True)
    objects = CustomUserManager()


    def __str__(self):
        return self.username

    
class Producto(models.Model):
    stock = models.IntegerField()
    descripcion = models.TextField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Bicicleta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    despacho = models.ForeignKey('Despacho', on_delete=models.CASCADE)

class Despacho(models.Model):
    estado = models.CharField(max_length=20)
    fecha_estimada = models.DateField()