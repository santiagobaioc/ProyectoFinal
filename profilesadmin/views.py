from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from profilesadmin.forms import FormRegistroUsuario, FormUsuarioEdicion, FormCambiarContraseña

# Create your views here.
class PaginaLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def get_success_url(self):
        return reverse_lazy('Inicio')
    
class PaginaRegistro(FormView):
    template_name = 'registro.html'
    form_class = FormRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(PaginaRegistro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Inicio')
        return super(PaginaRegistro, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormUsuarioEdicion
    template_name= 'usuarioEdicion.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        return self.request.user
    
class CambiarContraseña(PasswordChangeView):
    form_class = FormCambiarContraseña
    template_name = 'cambiarContraseña.html'
    success_url = reverse_lazy('cambio_exitoso')

def password_succes(request):
    return render(request, 'cambio_exitoso.html', {})
