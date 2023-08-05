from django.urls import path
from brandsapp import views
from .views import FoodActualizar 

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('marcaFormulario',views.marcaFormulario, name='MarcaFormulario'),
    path('marcaFoodLectura', views.marcaFoodLectura, name= 'MarcaFoodLectura' ),
    path('marcaFoodEliminar/<marca_nombre>', views.marcaFoodEliminar, name= 'MarcaFoodEliminar'),
    path('marcaFoodEditar/<int:pk>/', FoodActualizar.as_view(), name='MarcaFoodEditar'),
    path('expandirObjecto/<marca_nombre>', views.expandirObjeto, name='ExpandirObjeto')
]