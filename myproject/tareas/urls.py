from . import views
from django.urls import path, include

urlpatterns = [
    path("index/", views.index, name="index"),
    path("agregar/", views.agregar, name="agregar")
]
