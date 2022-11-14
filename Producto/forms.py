from django import forms
from Producto.models import PedidoProducto

class FormularioPedido(forms.ModelForm):
    
    class Meta:
        model = PedidoProducto
        fields = ('__all__')
        
class FomularioBusqueda(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)