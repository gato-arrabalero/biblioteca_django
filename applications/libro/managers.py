#IMportamos datetime para la conversion correcta de nuestra entradas de fechas
import datetime
#Importamos de django los models
from django.db import models
#Importamos la funcion Q para or y and
from django.db.models import Q,Count

# Clase que adentro tendran las funciones manager
class LibroManager(models.Manager):
    #Funciones Manager para el modelo Autor

#Funcion para genear un filtro x fecha
    def listar_libros(self, kword):
        #Variable=self_hace_referencia_a_todo_el_objeto_del_modelo.filter()
        resultado = self.filter(
            #Campo_de_nuestro_modelo__icontains = Parametro_que_le_estamos_pasando
            #Campo_de_nuestro_modelo__range = ('rango 1','rango2')
            titulo__icontains = kword,
            fecha__range = ('1900-01-01','2020-12-31')   
        )
        return resultado

#Filtrado x fecha    
    def listar_x_fecha(self,kword, fecha1, fecha2):
        #Conversion de datos de fechas al valor correcto
        #-->variable = datetime.datetime.strptime(variable,formato_de_conversion).date()--<
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()
        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = (date1 , date2)
        ) 
        return resultado
    
#Filtrar lobros por categoria pasando parmetro del ID de la tabla    
    def listar_libros_categoria(self, categoria):
        return self.filter(
            #la_fK__parametro_de_la_tabla_que_va_buscar = parametro_que_vamos_a_pasar
            categoria__id = categoria
        #order.by('parametro de nuestro modelo')
        ).order_by('titulo')

#Manager para ingresar un nuevo autor desde el codigo
    def add_autor_libro(self, libro_id, autor):
        #variable = self.funcion_get(parametro = valor que vamos a recuperar)
        libro = self.get(id = libro_id)
        #variable.parametro_de_nuestra_tabla_m2m.funcion_add(valor_del_parametro_agregar)
        #!!!!!!Para eliminar un autor en ves de add seria remove
        libro.autores.add(autor)
        return libro
 
#Manager para saber numero de veses fue prestado un libro
    def libros_prestamo(self):
#Variable = self.funcion_aggregate(variable = Count-->Metodo de contabilizar('valor inverso de nuestra FK'))
        resultado = self.aggregate(
            num_prestamos = Count('libro_prestamo')
        )
        return resultado


#Funcion manager como funciona annotate     
    def num_libros_prestados (self):
        resultado = self.annotate(
            num_prestados = Count('libro_prestamo')
        )

        for r in resultado:
            print('<------------------->')
            print (r , r.num_prestados)
 
        return resultado


#Manager para Categoria acceda a la tabla Autores

class CategoriaManager(models.Manager):
    def categoria_x_autor(self, autor):
        # '__' --> la doble raya significa que nos moivemos de una tabla a otra XD !!!!
        return self.filter(
#Nombre_del_valor_related_name__valor de la tabla que quermos__valor de la tabala que queremos
            categoria_libro__autores__id = autor
        ).distinct()
