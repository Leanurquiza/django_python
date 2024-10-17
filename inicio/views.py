from django.http import HttpResponse
from django.template import Template,Context,loader
from datetime import datetime
from django.shortcuts import render

def mi_vista (request):
    return HttpResponse('hola soy mi vista')


def inicio (request):
    return HttpResponse('<h1>Inicio Principal</h1>')


def vista_datos_1 (request,nombre):
    nombre_mayuscular=nombre.upper()
    return HttpResponse(f'Hola {nombre_mayuscular}')

def primer_template(request):
    
    archivo_del_template=open(r'templates/primer_template.html','r')
    
    template=Template(archivo_del_template.read())
    
    archivo_del_template.close()
    contexto= Context()
    
    render_template=template.render(contexto)
    
    return HttpResponse(render_template)


def segundo_template(request):
    
    fecha_actual=datetime.now()
    
    archivo_del_template=open(r'templates/segundo_template.html','r')
    
    template=Template(archivo_del_template.read())
    
    archivo_del_template.close()
    
    datos={'fecha_actual':fecha_actual}
    
    contexto= Context(datos)
    
    render_template=template.render(contexto)
    
    return HttpResponse(render_template)

def tercer_template(request):
    
    fecha_actual=datetime.now()
    datos={'fecha_actual':fecha_actual}
    
    template=loader.get_template('tercer_template.html')
    
    render_template=template.render(datos)

    return HttpResponse(render_template)    


def cuarto_template(request):
    fecha_actual=datetime.now()
    datos={'fecha_actual':fecha_actual,
           'numeros':list(range(1,11))}
    
    
    return render(request,'cuarto_template.html',datos)