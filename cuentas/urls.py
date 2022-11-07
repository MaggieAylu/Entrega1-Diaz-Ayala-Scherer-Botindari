from django.urls import path
from cuentas import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('registrar/', views.registrar, name = 'registrar'),
    path('pefil/', views.perfil, name = 'perfil'),
    path('pefil/editar', views.editar_perfil, name = 'editar_perfil'),
    path('logout/', LogoutView.as_view(template_name="cuentas/logout.html"), name = 'logout')
]
