from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class TipoSoli(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField(null=True)
    confirmacion = models.CharField(max_length=20, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    tipo_soli = models.ForeignKey(TipoSoli, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

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


class BiciReparacion(models.Model):
    modelo = models.CharField(max_length=50)
    comentarios = models.TextField()
    marca = models.CharField(max_length=20)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, null=True, blank=True)
    despacho = models.ForeignKey('Despacho', on_delete=models.CASCADE, null=True, blank=True)


class Bicicleta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    marca = models.CharField(max_length=20)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)
    despacho = models.ForeignKey('Despacho', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Despacho(models.Model):
    estado = models.CharField(max_length=20)
    fecha_estimada = models.DateField()