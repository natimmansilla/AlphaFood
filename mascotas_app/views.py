from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota 

def inicio(request):
    return HttpResponse('<h1>REGISTRO DE MASCOTAS</H1>')

def uno(request):
    return render (request, 'paginas/uno.html')

def mascotas(request):
    mascotas=Mascota.objects.all()
    print(mascotas)
    return render (request, 'mascotas/index.html', {'mascotas':mascotas})

def registrar(request):
    return render(request, 'mascotas/registrar.html')

def editar(request):
    return render(request, 'mascotas/editar.html')
