from django.urls import path
from AppCoder.views import * #inicio,cursos,entregables,estudiantes,profesores,setEstudiantes, getEstudiantes, buscarEstudiante

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos, name="Cursos"),
    path('entregables/', entregables,name="Entregables"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('setEstudiante/', setEstudiantes, name="setEstudiante"),
    path('getEstudiante/', getEstudiantes, name="getEstudiante"),
    path('buscarEstudiante/', buscarEstudiante, name="buscarEstudiante"),
]