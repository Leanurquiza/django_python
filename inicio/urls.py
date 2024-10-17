from django.urls import path
from inicio.views import mi_vista,inicio,vista_datos_1,primer_template,segundo_template,tercer_template,cuarto_template

urlpatterns = [
    path('mi-vista/',mi_vista),
    path('',inicio),
    path('vista-datos1/<nombre>/',vista_datos_1),
    path('primer-template',primer_template),
    path('segundo-template',segundo_template),
    path('tercer-template',tercer_template),
    path('cuarto-template',cuarto_template)
    
]
