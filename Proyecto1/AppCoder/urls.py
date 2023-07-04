from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import * #inicio,cursos,entregables,estudiantes,profesores,setEstudiantes, getEstudiantes, buscarEstudiante

urlpatterns = [
    path('', loginWeb),
    path('inicio/', inicio),
    path('cursos/', cursos, name="Cursos"),
    path('entregables/', entregables,name="Entregables"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('setEstudiante/', setEstudiantes, name="setEstudiante"),
    path('getEstudiante/', getEstudiantes, name="getEstudiante"),
    path('buscarEstudiante/', buscarEstudiante, name="buscarEstudiante"),
    path('eliminarEstudiante/<nombre_estudiante>', eliminarEstudiante, name="eliminarEstudiante"),
    path('editarEstudiante/<nombre_estudiante>', editarEstudiante, name="editarEstudiante"),
    path('editarEstudiante/<nombre_estudiante>', editarEstudiante, name="editarEstudiante"),
    path('login/', loginWeb, name="login"),
    path('registro/', registro, name="registro"),
    path('Logout/',LogoutView.as_view(template_name = 'AppCoder/login.html'), name="Logout"),
    path('perfil/', perfilview, name="perfil"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword, name="changePassword"),
    path('Perfil/Avatar/', editAvatar, name="editAvatar"),
]