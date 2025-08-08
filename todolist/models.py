from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    encargado = models.ForeignKey(Usuario, on_delete=models.CASCADE, null = False, blank = False, default=None )
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
    