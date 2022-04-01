from django.http import HttpResponse
from datetime import datetime, date
from django.template import *


def saludo(request):
    return HttpResponse('Hola Django-Coder')

def segunda_vista(resquest):
    return HttpResponse('<br><br> ya tengo esto')

def dia_hoy(request):
    dia = datetime.datetime.now()

    docu = f'hoy es {dia}'
    return HttpResponse(docu)

def nombre_es(self, nombre):
    
    docu = f'Mi nombre es: <br> {nombre}'

    return HttpResponse(docu)

def fecha_actual(request, fecha):

    fecha = date.today()

    anio = fecha.year()

    fecha = int(fecha)


def probandoTemplate(self):

    nombre = "Fer"
    ap = "Kova"
    
    lista_notas = [2, 3, 3, 5, 6]

    diccionario = {"nombre":nombre, "apellido": ap, 'hoy': datetime.datetime.now, 'lista_notas': lista_notas} #<-----Para enviar al contexto
    miHtml= open("C:/Users/ferchu/Documents/Django/Django-coder/Proyecto1/Proyecto1/Plantilla/template1.html")
    
    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento
    
    miHtml.close() #Cerramos el archivo
    
    miContexto = Context(diccionario) #le doy al contexto mi nombre y apellido
    
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    
    return HttpResponse (documento)
    
    #ahora haremos referencia a lo enviado en el diccionario
    