from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_encuesta, name='formulario_encuesta'),  # Ruta principal
    path('gracias/', views.gracias, name='gracias'),  # Ruta para la página de gracias
    # Añadir otras rutas aquí
]
