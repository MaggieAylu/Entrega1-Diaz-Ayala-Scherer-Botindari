from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class PedidoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    resumen = models.TextField(null = True)
    blog_post = RichTextField(null = True)
    banner = models.ImageField(blank=True, null = True, upload_to= 'images/')
    status = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre}'
    