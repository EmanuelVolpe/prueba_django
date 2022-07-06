from . import views
from django.urls import path, include

urlpatterns = [
    path("index/", views.index, name="index"),
    path("saludo/<str:nombre>", views.saludo, name="saludo")
]
