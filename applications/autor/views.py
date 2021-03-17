from django.shortcuts import render

#Importacion listas genericas
from django.views.generic import ListView
#Modelo local
from .models import Autor
# Create your views here.


class ListAutores(ListView):    
    context_object_name = 'lista_autores'
    template_name = "autor/lista.html"

    def get_queryset(self):
        #Logica para el filtro
        #Variable= self.request.Metodo_a_interceptar.get(tupla-->Identificador,'')
        palabra_clave = self.request.GET.get('kword','')
        #Modelo.objects.nombre_de_la_funcion_manager(Variable_que_se_recoge_de_la_caja_de_texto=paramtro_funcion_manager)
        return Autor.objects.buscar_autor4(palabra_clave)

