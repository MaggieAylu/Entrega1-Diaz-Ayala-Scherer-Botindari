from django.urls import path
from Producto import views

urlpatterns = [
    path('', views.Home, name='Home' ),
    path('about/', views.AboutUs, name='about'),
    path('producto/', views.CargarProducto, name='producto' ),
    path('pedido/', views.VerPedido, name='pedido'),
]