from django.shortcuts import render

# Create your views here.

tareas = ["foo", "bar", "baz"]

# Create your views here.


def index(request):
    return render(request, "index.html", {
        "titulo": "TAREAS",
        "tareas": tareas
    })

# Agrega una nueva tarea:


def agregar(request):
    return render(request, "agregar.html", {
        "titulo": "AGREGAR TAREA"
    })
