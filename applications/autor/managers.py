#Importamos de django los models
from django.db import models
#Importamos la funcion Q para or y and
from django.db.models import Q

# Clase que adentro tendran las funciones manager
class AutorManager(models.Manager):
    #Funciones Manager para el modelo Autor

#Funcion para genear un filtro
    def buscar_autor(self, kword):
        #Variable=self_hace_referencia_a_todo_el_objeto_del_modelo.filter()
        resultado = self.filter(
            #Campo_de_nuestro_modelo+_icontains = Parametro_que_le_estamos_pasando
            #Nota!!! __icontains viene siendo como %like% de sql pero en el ORM
            nombre__icontains = kword 
        )
        return resultado


#Funcion para generar un filtro pero con OR o sea uno u otro
    def buscar_autor2(self, kword):        
        resultado = self.filter(
            #Q(Campo_de_nuestro_modelo+_icontains = Parametro_que_le_estamos_pasando)+
            # |-->viene siendo or + Q(Campo_de_nuestro_modelo+_icontains = Parametro_que_le_estamos_pasando)
            Q(nombre__icontains = kword) | Q(apellido__icontains = kword) 
        )
        return resultado


#Funcion para generar un filtro con exclusion de un campo de la taba
    def buscar_autor3(self, kword):         
        resultado = self.filter(
            #Campo_de_nuestro_modelo+_icontains = Parametro_que_le_estamos_pasando
            # .exclude(campo_de_la_tabla = valor_que_sera_igualado)
            nombre__icontains = kword 
        ).exclude(edad=67)#--->exclude puede ser usado igual con or o tambien otro filter sobre mi filter xd!!
        return resultado

        
#Funcion para gnenerar un filtro > que < que y el uso de and        
    def buscar_autor4(self, kword):
        resultado = self.filter(
            #__gt --> mayor que    ___lt --> menor que 
            #la coma , --> es nuestra and &
            edad__gt = 45,
            edad__lt = 60
        ).order_by('apellido')#  --> el order_by es como en SQL (campo_de_nuestro_modelo)
        return resultado

