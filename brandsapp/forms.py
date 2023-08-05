from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from brandsapp.models import Marca

class MarcaFormulario(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('categoria', 'nombre', 'descripcion', 'email', 'imagenes')

        widgets = {
            'category' : forms.Select(attrs={'class': 'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'contactNumber' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
             }
        
class MarcaEditar(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ('categoria', 'nombre', 'descripcion', 'email', 'imagenes')

        widgets = {
            'categoria' : forms.Select(attrs={'class': 'form-control'}),
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            #'imagenes': forms.ImageField(attrs={'class':'form-control'})
                        
        }