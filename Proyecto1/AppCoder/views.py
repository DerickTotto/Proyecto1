from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppCoder.models import Estudiante
from AppCoder.forms import formSetEstudiante

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    Estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html",{"Estudiantes": Estudiantes})

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def setEstudiantes(request):
    Estudiantes = Estudiante.objects.all()
    #return render(request, "AppCoder/estudiantes.html",{"Estudiantes": Estudiantes})
    if request.method == 'POST':
        estudiante = Estudiante(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
        estudiante.save()  
        miFormulario = formSetEstudiante()  
        return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario, "Estudiantes":Estudiantes})
    else:
        miFormulario = formSetEstudiante()
    return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario, "Estudiantes":Estudiantes})

    """if request.method == 'POST':
        estudiante = Estudiante(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
        estudiante.save()
        return render(request,"AppCoder/inicio.html")
    return render(request, "AppCoder/setEstudiantes.html")"""

def getEstudiantes(request):
    return render(request, "AppCoder/getEstudiantes.html")

def buscarEstudiante(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre = nombre)
        return render(request, "AppCoder/getEstudiantes.html", {"estudiantes":estudiantes, "key": "value"})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)

def eliminarEstudiante(request, nombre_estudiante):
    estudiante = Estudiante.objects.get(nombre= nombre_estudiante)
    estudiante.delete()
    miFormulario = formSetEstudiante()
    Estudiantes = Estudiante.objects.all()
    return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario, "Estudiantes":Estudiantes})

def editarEstudiante(request, nombre_estudiante):
    estudiante = Estudiante.objects.get(nombre= nombre_estudiante)
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data

            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()
            miFormulario = formSetEstudiante()
            Estudiantes = Estudiante.objects.all()
            return render(request, "AppCoder/setEstudiantes.html", {"miFormulario":miFormulario, "Estudiantes":Estudiantes})
    else:
        miFormulario = formSetEstudiante()
    return render(request, "AppCoder/editarEstudiante.html", {"miFormulario":miFormulario})