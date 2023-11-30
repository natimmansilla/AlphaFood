from django.urls import path
from . import views

app_name = "mascotas_app"

urlpatterns= [
    path ('', views.mascotas, name='inicio'), 
    path ('uno', views.uno, name='uno'),

    path ('mascotas', views.mascotas, name='mascotas'),
    path('mascotas/registrar', views.registrar, name='registrar'),
    path('mascotas/editar', views.editar, name='editar'),
]