from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.

tareas = ["foo", "bar", "baz"]


class FormularioNuevaTarea(forms.Form):
    tarea = forms.CharField(label="Nueva Tarea")
    prioridad = forms.IntegerField(
        label="prioridad", min_value=1, max_value=10)

# Create your views here.


def index(request):
    return render(request, "index.html", {
        "titulo": "TAREAS",
        "tareas": tareas
    })

# Agrega una nueva tarea:


def agregar(request):
    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = FormularioNuevaTarea(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            tarea = form.cleaned_data["tarea"]

            # Add the new task to our list of tasks
            tareas.append(tarea)

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("index"))

        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {
                "titulo": "AGREGAR TAREA",
                "form": form
            })
    return render(request, "agregar.html", {
        "titulo": "AGREGAR TAREA",
        "form": FormularioNuevaTarea()
    })
