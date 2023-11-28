from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<h1>REGISTRO DE MASCOTAS</H1>')
