from django.views.generic import TemplateView
from django.shortcuts import render

class IndexPage(TemplateView):
    template_name = "index.html"

def menus(request):
    return render(request, 'index.html', {'scroll_to_id': 'menus'})

def instrucciones(request):
    return render(request, 'index.html', {'scroll_to_id': 'instrucciones'})

def preguntas(request):
    return render(request, 'index.html', {'scroll_to_id': 'preguntas'})

def donde_estamos(request):
    return render(request, 'index.html', {'scroll_to_id': 'dondeEstamos'})

def contacto(request):
    return render(request, 'index.html', {'scroll_to_id': 'contacto'})
    