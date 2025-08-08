from rest_framework import serializers
from .models import Tarea

class POSTTareaRequest(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['titulo', 'estado', 'descripcion']
        read_only_fields = ['estado']


class PATCHTareaRequest(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'estado', 'descripcion']
        read_only_fields = ['id', 'titulo', 'descripcion']

class DELETETareaRequest(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'estado', 'descripcion']
        read_only_fields = ['titulo', 'estado', 'descripcion']