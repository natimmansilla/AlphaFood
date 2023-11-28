from django.urls import path
from . import views

app_name = "mascotas_app"

urlpatterns= [
    path ('', views.inicio, name='inicio'), 
    path ('uno', views.uno, name='uno'),
    path ('mascotas', views.mascotas, name='mascotas'),
]