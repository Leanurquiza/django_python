from django.urls import path
from inicio.views import mi_vista,crear_auto,template_2,inicio

urlpatterns = [
    path('mi-vista/',mi_vista),
    path('crear-auto/<marca>/<modelo>/<anio>',crear_auto),
    path('cuarto-template',template_2),
    path('inicio/',inicio)
    
]
