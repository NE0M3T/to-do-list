from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo