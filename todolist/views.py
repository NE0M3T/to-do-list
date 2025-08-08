from rest_framework import viewsets
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
 
from .models import Tarea, Usuario
from .responses import TareaSerializer, UsuarioSerializer
from .requests import POSTUsuarioRequest, PATCHUsuarioRequest, DELETEUsuarioRequest

# Create your views here.

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(methods=['get'], detail=False, url_path='deshabilitadas')
    def deshabilitada(self, request):
        tareas = self.queryset.filter(estado=False)
        serializer = self.serializer_class(tareas, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True)
    def usuarios(self, request, pk=None):
        tareas = self.queryset.filter(encargado_id=pk)
        serializer = self.serializer_class(tareas, many=True)
        return Response(serializer.data)


class GETUsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter()
    serializer_class = UsuarioSerializer
    http_method_names = ['get']

    @swagger_auto_schema(
        operation_summary="Listar usuarios",
        operation_description="Lista todos los usuarios"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Obtener usuario por ID",
        operation_description="Devuelve un usuario por su ID"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class POSTUsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = POSTUsuarioRequest
    http_method_names = ['post']

    @swagger_auto_schema(
        operation_summary="Crear un usuario",
        operation_description="Crear un nuevo usuario",
        request_body=POSTUsuarioRequest
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
        
class PATCHUsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = PATCHUsuarioRequest
    http_method_names = ['patch']
    
    @swagger_auto_schema(
        operation_summary="Actualizar un usuario",
        operation_description="Actualiza los datos de un usuario",
        request_body=PATCHUsuarioRequest
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
class DELETEUsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = DELETEUsuarioRequest
    http_method_names = ['delete']

    @swagger_auto_schema(
        operation_summary="Eliminar un usuario",
        operation_description="Elimina un usuario por ID"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get']

    @swagger_auto_schema(
        method='get',
        operation_summary="Listar tareas de un usuario",
        operation_description="Devuelve todas las tareas cuyo responsable coincide con el ID del usuario."
    )
    @action(detail=True, methods=['get'], url_path='tareas')
    def tareas(self, request, pk=None):
        tareas_qs = Tarea.objects.filter(encargado_id=pk).order_by('id')
        serializer = TareaSerializer(tareas_qs, many=True)
        return Response(serializer.data)
