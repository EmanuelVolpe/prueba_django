from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def saludo(request, nombre):
    return render(request, "saludo.html", {
        "nombre": nombre.capitalize(),
        "titulo": "HOLA"
    })
