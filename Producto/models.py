from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class PedidoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_de_producto = models.CharField(max_length=100)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}'
    