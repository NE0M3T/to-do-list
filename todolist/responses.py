from rest_framework import serializers
from .models import Tarea, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido']

class TareaSerializer(serializers.ModelSerializer):
    encargado = UsuarioSerializer(read_only=True)
    class Meta:
        model = Tarea
        fields = "__all__"