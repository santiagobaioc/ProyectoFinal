from django.urls import path
from profilesadmin import views
from django.contrib.auth.views import LogoutView
from .views import PaginaLogin, PaginaRegistro, UsuarioEdicion, CambiarContraseña
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    
    path('login/', PaginaLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', PaginaRegistro.as_view(), name='registro'),
    path('usuarioEdicion/', UsuarioEdicion.as_view(), name='usuarioEdicion'),
    path('cambiarContraseña/', CambiarContraseña.as_view(), name='cambiarContraseña'),
    path('cambio_exitoso/' , views.password_succes, name='cambio_exitoso'),
    
]