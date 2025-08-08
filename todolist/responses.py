from rest_framework import serializers
from .models import Tarea

class GETTareaResponse(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'estado', 'descripcion']
        read_only_fields = ['id', 'titulo', 'estado', 'descripcion']
        methods = ['GET']
        