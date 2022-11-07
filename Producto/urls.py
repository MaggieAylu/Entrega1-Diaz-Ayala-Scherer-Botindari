from django.urls import path
from Producto import views

urlpatterns = [
    path('', views.Home, name='Home' ),
    path('about/', views.AboutUs, name='about'),
    path('producto/', views.CargarProducto, name='cargar-producto' ),
    path('pedido/', views.VerPedido, name='pedido'),
    path('pedido/eliminar/<int:id>', views.EliminarProducto, name='eliminar_producto'),
    path('pedido/editar/<int:pk>', views.EditarProducto.as_view(), name="editar_producto")
]