from asyncio import AbstractServer
from django.db import models

class Solicitud(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    confirmacion = models.BooleanField()
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=80)
    es_cliente = models.BooleanField()
    es_tecnico = models.BooleanField()
    es_vendedor = models.BooleanField()

    def __str__(self):
        return str(self.nombre)
    
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