from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def familiar(request, nombre, apellido, edad, nacimiento):

    familiar = Familiar(nombre = nombre, apellido = apellido, edad = edad, fecha_de_nacimiento = nacimiento)
    familiar.save()

    return HttpResponse(f"""
        <ul><p>
        <h3><br><br>Nombre: {familiar.nombre}<br><br>Apellido: {familiar.apellido}<br><br>Edad: {familiar.edad}<br><br>Fecha de nacimiento (año-mes-día): {familiar.fecha_de_nacimiento}<br></h3>
        <h1 style="color: blue;">Añadido</h1>
        </p></ul>
    """)



def lista_familiares(request):

    lista = Familiar.objects.all()
    return render(request, "lista_familiares.html", {"lista_familiares": lista})