from django.db import models
#Model de una de nuestra FK many to many
from applications.autor.models import Autor
# Importamos el manager
from .managers import LibroManager, CategoriaManager


#Modelo de la tabla Categoria

class Categoria (models.Model):
    nombre = models.CharField(
        max_length=50
    )
    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + '--->' +self.nombre


#Modelo de la tabla Libro

class Libro (models.Model):
    titulo = models.CharField(
        max_length=100
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        #parametro cuando usamos un FK para movernos de manera inversa='string'             
        related_name='categoria_libro'
    )   

    autores = models.ManyToManyField(Autor)

    fecha = models.DateField('fecha de lanzamiento')

    portada = models.ImageField(
        upload_to='portada',
        height_field=300,
        width_field=200,
        max_length=800,
        blank = True,
    )

    visitas = models.PositiveIntegerField()

    #Conectamos el Manager --> contante_objects = nombre_del_manager

    objects = LibroManager()

    def __str__(self):
        return str(self.id)+ '---->' +self.titulo

