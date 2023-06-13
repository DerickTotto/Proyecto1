from django.urls import path
from AppCoder.views import inicio,cursos,entregables,estudiantes,profesores

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('estudiantes', estudiantes),
    path('profesores/', profesores),
]