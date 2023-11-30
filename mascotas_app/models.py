from django.db import models

class Mascota(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=False, blank=False)
    edad = models.IntegerField(verbose_name="Edad", null=False, blank=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso", null=False, blank=False)
    raza = models.CharField(max_length=100, verbose_name="Raza", null=False, blank=False)
    email = models.EmailField(verbose_name="Email", null=False, blank=False)

   
