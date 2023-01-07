from django.urls import path, re_path
from django.conf.urls import include

# Importacion de vistas
from Conjunto_Relaciones_api.views import RelacionesConjuntos, EjercicioRelacion, ValidacionConjunto

urlpatterns = [
   re_path(r'^/relacion/obtener-rel/$', RelacionesConjuntos.as_view()),
   re_path(r'^/relacion/ejercicio/$', EjercicioRelacion.as_view()),
   re_path(r'^/relacion/validar/$', ValidacionConjunto.as_view()),
]