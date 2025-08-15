from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', default='default-product.jpg')

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.CharField(max_length=255,default='usuario_default')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=50,
        choices=[
            ('Pendiente', 'Pendiente'),
            ('En proceso', 'En proceso'),
            ('Enviado', 'Enviado'),
            ('Completado', 'Completado'),
            ('Cancelado', 'Cancelado'),
        ],
        default='Pendiente' 
    )
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

    def __str__(self):
        return f'Pedido #{self.id} - {self.usuario}'
