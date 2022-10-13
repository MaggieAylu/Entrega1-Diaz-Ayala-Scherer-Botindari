from django.db import models

# Create your models here.

class PedidoProducto(models.Model):
    nombre = models.CharField()
    tipo_de_producto = models.CharField()
    precio = models.IntegerField()
    