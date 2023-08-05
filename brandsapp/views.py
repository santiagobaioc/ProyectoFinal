from django.shortcuts import render
from brandsapp.models import Marca
from django.http import HttpResponse
from brandsapp.forms import MarcaFormulario, MarcaEditar
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    
    return render (request,"inicio.html") 

@login_required
def marcaFormulario(request):
      if request.method == "POST":
          miFormulario=MarcaFormulario(request.POST, request.FILES) 
          print(miFormulario)
          if miFormulario.is_valid():
              informacion = miFormulario.cleaned_data
              marca = Marca(categoria= informacion['categoria'],
                        nombre=informacion['nombre'],
                        descripcion=informacion['descripcion'],
                        email=informacion['email'],
                        imagenes=request.FILES['imagenes'])
              marca.save()
              return render(request, 'inicio.html')
      else:
          miFormulario=MarcaFormulario()
      return render(request, "marcaFormulario.html",{"miFormulario":miFormulario})

def marcaFoodLectura(request):
    food=Marca.objects.filter(categoria__startswith='food')
    context={"food":food}
    return render(request, 'marcaFoodLectura.html', context)

def marcaFoodEliminar(request, marca_nombre):
    food= Marca.objects.filter(nombre__startswith=marca_nombre)
    food.delete()

    foods = Marca.objects.filter(categoria__startswith='food')  
 
    context = {"foods": foods}
 
    return render(request, "inicio.html", context)

class FoodActualizar(LoginRequiredMixin, UpdateView):
    model = Marca
    form_class = MarcaEditar
    success_url = reverse_lazy('MarcaFoodLectura')
    context_object_name = 'food'
    template_name = 'marcaFoodEditar.html'
@login_required
def expandirObjeto(request, marca_nombre):
    food=Marca.objects.filter(nombre__startswith=marca_nombre)
    context={'food':food}
    return render(request, 'expandirObjeto.html', context)