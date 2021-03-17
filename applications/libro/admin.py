from django.contrib import admin
#Modelo de la aplicacion
from .models import Libro,Categoria
# Register your models here.
admin.site.register(Libro)
admin.site.register(Categoria)