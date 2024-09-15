from django.db import models

class Encuesta(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    puntuacion = models.IntegerField()
    comentarios = models.TextField()

    def __str__(self):
        return self.nombre
