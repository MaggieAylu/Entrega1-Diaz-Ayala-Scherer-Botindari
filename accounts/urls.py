from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('registrar/', views.registrar, name = 'registrar'),
    path('logout/', LogoutView.as_view(template_name="cuentas/logout.html"), name = 'logout'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('perfil/editar/', views.editar_perfil, name = 'editar_perfil'),
    path('perfil/cambiar-contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
]
