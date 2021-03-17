from django.contrib import admin
from django.urls import path

#Importar nuestras Vistas

from . import views



urlpatterns = [
    path('autores/', 
    views.ListAutores.as_view(),
    name='Autores'
    ),
]
 