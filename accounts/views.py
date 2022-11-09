from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as djlogin
from accounts.forms import FormularioRegistro, FormularioEditarPerfil
from django.contrib.auth.decorators import login_required

#Iniciar sesión
def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            djlogin(request, usuario)
            return redirect ('Home')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario':formulario})

#Registrarse
def registrar(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ('Home')
    else:
        formulario = FormularioRegistro()
   
    return render(request, 'accounts/registrar.html', {'formulario':formulario})

#Perfil de usuario
@login_required
def perfil(request):
    
    return render(request, 'accounts/perfil.html', {})

#Editar Perfil
@login_required
def editar_perfil(request):
    
    if request.method == 'POST':
        formulario = FormularioEditarPerfil(request.POST)
        
        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            request.user.first_name = data_nueva['first_name']
            request.user.last_name = data_nueva['last_name']
            request.user.email = data_nueva['email']
            
            request.user.save()
            return redirect('perfil')
    
    else:
        formulario = FormularioEditarPerfil(
            initial={
                'first_name': request.user.first_name, 
                'last_name': request.user.last_name, 
                'email': request.user.email
                }
             )
    return render(request, 'accounts/editar_perfil.html', {'formulario':formulario})