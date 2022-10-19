from django.db import models

# Create your models here.

class Familiar (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False)