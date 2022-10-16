from dataclasses import field
from django import forms
from Producto.models import PedidoProducto

class FormularioPedido(forms.ModelForm):
    
    class Meta:
        model = PedidoProducto
        fields = ('__all__')