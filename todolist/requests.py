from rest_framework import serializers
from .models import Tarea, Usuario

class POSTTareaRequest(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['titulo', 'estado', 'encargado', 'descripcion']
        read_only_fields = ['estado']


class PATCHTareaRequest(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'estado','encargado', 'descripcion']
        read_only_fields = ['id', 'titulo','encargado', 'descripcion']

class DELETETareaRequest(serializers.Serializer):
    id = serializers.IntegerField()

class POSTUsuarioRequest(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido']

class PATCHUsuarioRequest(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido']
        read_only_fields = ['id']

class DELETEUsuarioRequest(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellido']
        read_only_fields = ['nombre', 'apellido']