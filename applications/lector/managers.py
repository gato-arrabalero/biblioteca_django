#Importamos de django los models
from django.db import models
#Importamos la funcion Q para or y and
from django.db.models import Q,Count, Avg

class PrestamoManager(models.Manager):
    #Funciones para prestamo y como usar aggregate
    def libros_promedio_lectores_edad(self):
#variable = self.filter-->para filtrar (variable__parametro de la tabla = en este caso el indice)
        resultado = self.filter(
            libro__id = '1'
#.funcion aggregate (variable = funcioj de promedio AVG ( tabla__parametro de la tabla)) 
        ).aggregate(
            promedio_edad = Avg('lector__edad')
        )
        return resultado

#Funcion del annottate y values
    def num_libros_prestados (self):
    #variable = self.values(parametro de nuestro modelo).annotate(variable= Count(Prametro de nuestro modelo))
        resultado = self.values(
            'libro'
        ).annotate(
            num_prestados = Count('libro')
        )
    #For en variable_contenedora--> imprimimos r-->varibel iterarora,variable[como es un diccionario acceder a la clave]
        for r in resultado:
            print('<------------------->')
            print (r , r['num_prestados'])
 
        return resultado