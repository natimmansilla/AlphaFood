from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<h1>REGISTRO DE MASCOTAS</H1>')

def uno(request):
    return render (request, 'paginas/uno.html')

def mascotas(request):
    return render (request, 'mascotas/index.html')
