from django.db import models

# Create your models here.
#Importar nuestros manager para este modelo
from .managers import AutorManager
#Modelo de la tabla Autor

class Autor(models.Model):
    nombre = models.CharField(
        max_length=50
    )

    apellido = models.CharField(
        max_length=50
    )

    nacionalidad = models.CharField(
        max_length=50
    )

    edad = models.PositiveIntegerField() 

    #Manger enlazado a nuestro modelo
    objects = AutorManager()

    def __str__(self):
        return str(self.id)+'----->'+self.nombre + '----->' + self.apellido    
