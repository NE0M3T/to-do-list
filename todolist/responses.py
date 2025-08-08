from rest_framework import serializers
from .models import Tarea, Usuario

class GETTareaResponse(serializers.ModelSerializer):
    encargado = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'estado', 'encargado', 'descripcion']
        
class GETUsuarioResponse(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido']