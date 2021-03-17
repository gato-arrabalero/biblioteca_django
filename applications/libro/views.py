from django.shortcuts import render

#Importacion listas genericas
from django.views.generic import ListView,DetailView
#Modelo local
from .models import Libro
# Create your views here.


class ListLibros(ListView):    
    context_object_name = 'lista_libros'
    template_name = "libros/lista.html"
    
    def get_queryset(self):
        #Logica para el filtro
        #Variable= self.request.Metodo_a_interceptar.get(tupla-->Identificador,'')
        palabra_clave = self.request.GET.get('kword','')
        #obtencion de valores de fecha1
        f1 = self.request.GET.get('fecha1','')
        #Obtencion de valores de fecha2
        f2 = self.request.GET.get('fecha2','')
        #Validacion
        if f1 and f2:
                return Libro.objects.listar_x_fecha(palabra_clave,f1,f2)
        else:
                return Libro.objects.listar_libros(palabra_clave)

class ListLibros2(ListView):
        context_object_name = 'lista_libros'
        template_name = 'libros/lista2.html'

        def get_queryset(self):
                return Libro.objects.listar_libros_categoria('4')



class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/detalle.html"
