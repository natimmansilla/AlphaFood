from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Mascota 
from .forms import MascotaForm

def inicio(request):
    return HttpResponse('<h1>REGISTRO DE MASCOTAS</H1>')

def uno(request):
    return render (request, 'paginas/uno.html')

def mascotas(request):
    mascotas=Mascota.objects.all()
    return render (request, 'mascotas/index.html', {'mascotas':mascotas})

def registrar(request): 
    formulario= MascotaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        mascota_nueva = formulario.save()
        return redirect ('mascotas_app:mascotas')
    return render(request, 'mascotas/registrar.html', {'formulario': formulario})

def editar(request, id):
    mascota=Mascota.objects.get(id=id)
    formulario=MascotaForm(request.POST or None, request.FILES or None, instance=mascota)
    return render(request, 'mascotas/editar.html', {'formulario': formulario})

def eliminar(request, id):
    mascota = Mascota.objects.get(id= id)
    mascota.delete()
    return redirect ('mascotas_app:mascotas')
