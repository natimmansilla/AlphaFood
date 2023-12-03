
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import IndexPage
from .views import (
    menus,
    instrucciones,
    preguntas,
    donde_estamos,
    contacto
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexPage.as_view(), name="index"),
    path("mascotas/", include("mascotas_app.urls", namespace="mascotas_app")),
    path('menus/', menus, name='menus'),
    path('instrucciones/', instrucciones, name='instrucciones'),
    path('preguntas/', preguntas, name='preguntas'),
    path('donde-estamos/', donde_estamos, name='dondeEstamos'),
    path('contacto/', contacto, name='contacto'),
]
