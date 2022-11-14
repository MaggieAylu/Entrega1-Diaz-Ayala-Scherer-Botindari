from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Producto.models import PedidoProducto
from Producto.forms import FormularioPedido, FomularioBusqueda
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Pagina de inicio
def Home(request):
    return render(request, 'Producto/Home.html',{})

#Pagina de Sobre Nosotros
def AboutUs(request):
    return render(request, 'Producto/AboutUs.html',{})


#Cargar productos por medio de formulario
@login_required
def CargarProducto(request):
    if request.method == "POST":
        
        formulario = FormularioPedido(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            pedido = PedidoProducto(
            
                nombre = data["nombre"],
                author = data['author'],
                resumen = data['resumen'],
                blog_post = data['blog_post'],
                banner = data['banner'],
                status = data['status'],
                date_added = data['date_added'],
            )
            
            pedido.save()
            
            return redirect('pedido')

    formulario = FormularioPedido()  
    return render(request, 'Producto/PedidoProductos.html', {'formulario': formulario})


#Ver lista de productos
def VerPedido(request):
    
    nombre = request.GET.get('nombre', None)
    if nombre: 
        pedido=PedidoProducto.objects.filter(nombre__icontains = nombre)
    else: 
        pedido = PedidoProducto.objects.all()
    
    formulario1 = FomularioBusqueda()
    
    template = loader.get_template('Producto/listadepedido.html')
    render_template = template.render({'pedido': pedido, 'formulario1': formulario1})
    return HttpResponse(render_template)


#Eliminar de la lista
@login_required
def EliminarProducto(request, id):
    producto = PedidoProducto.objects.get(id=id)
    producto.delete()
    return redirect ('pedido')

#Editar lista de productos
class EditarProducto(LoginRequiredMixin,UpdateView):
    model = PedidoProducto
    success_url = '/Producto/listadepedido.html'
    template_name = 'Producto/editarproducto.html'
    fields = ['nombre','author','resumen','blog_post','banner']


context = {
    'nombre' : 'Blog Site'}

def view_post(request,pk=None):
    context['nombre'] = ""
    if pk is None:
        messages.error(request,"Unabale to view Post")
        return redirect('Home')
    else:
        post = PedidoProducto.objects.filter(id = pk).first()
        context['nombre'] = post.nombre
        context['pedido'] = post
        return render(request, 'Producto/verproducto.html',context)
    
