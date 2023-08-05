from django.db import models


# Create your models here.
class Marca(models.Model):
    clasificacion=(('food','Food'), 
                    ('deportes','Deportes'),
                    ('cuidado_personal', 'Cuidado Personal'),
                     ('tecnología', 'Tecnología'),
                     ('autos', 'Autos'),
                      ('otro', 'Otro'))
    categoria= models.CharField(max_length=30, choices=clasificacion, default='Food')
    nombre=models.CharField(max_length=30)
    descripcion=models.TextField(null=True, blank=True)
    fecha_publicacion=models.DateField (auto_now_add=True)
    email = models.EmailField()
    imagenes = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    def __str__(self):
        
        return f"Categoria: {self.categoria} - Nombre: {self.nombre} - Fecha de Publicación: {self.fecha_publicacion}"