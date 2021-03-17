from django.contrib import admin
#Importamos los Modelos
from .models import Lector, Prestamo

admin.site.register(Lector)
admin.site.register(Prestamo)