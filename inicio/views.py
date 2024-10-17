from django.http import HttpResponse
from django.template import Template,Context,loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import Auto

def mi_vista (request):
    return HttpResponse('hola soy mi vista')

def template_2(request):
    fecha_actual=datetime.now()
    datos={'fecha_actual':fecha_actual,
           'numeros':list(range(1,11))}
    
    
    return render(request,'cuarto_template.html',datos)

def crear_auto(request,marca,modelo,anio):
    
    auto=Auto(marca=marca,modelo=modelo,anio=anio)
    auto.save()


    return render(request,'crear_auto.html',{'auto':auto})

def inicio(request):
    return render(request,'index.html')