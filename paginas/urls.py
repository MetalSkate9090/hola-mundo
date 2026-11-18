from django.urls import path
from .views import vista_inicio, vista_acerca_de

urlpatterns = [
    path("", vista_inicio, name="inicio"),
    path("acerca-de/", vista_acerca_de, name="acerca_de"),
]