from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return("Vista profesores")

def estudiantes(request):
    return("Vista estudiantes")

def entregables(request):
    return("Vista entregables")