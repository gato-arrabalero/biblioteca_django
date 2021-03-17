from django.db import models
from applications.libro.models import Libro
#Importar los managers

from .managers import PrestamoManager
# Create your models here.

#Modelo de la tabla lector

class Lector (models.Model):
    nombre = models.CharField(
        max_length=50
    )

    apellido = models.CharField(
        max_length=50
    )

    nacionalidad = models.CharField(
        max_length=50
    )
    
    edad = models.PositiveIntegerField(default=0) #Valida que si no recibe edad automaticamente sea 0

    def __str__(self):
        return self.nombre + '' + self.apellido


#Modelo de la tabla Prestamo

class Prestamo (models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE,
        
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name= 'libro_prestamo'
    )

    fecha_prestamo = models.DateField()

    fecha_devolucion = models.DateField(
        blank=True,
        null=True
    )

    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def __str__(self):
        return self.libro.titulo