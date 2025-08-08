from rest_framework import viewsets
from rest_framework.response import Response
 
from .models import Tarea
from .responses import GETTareaResponse
from .requests import POSTTareaRequest, PATCHTareaRequest, DELETETareaRequest

# Create your views here.

class GETTareaView(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = GETTareaResponse
    http_method_names = ['get'] 

class POSTTareaView(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = POSTTareaRequest
    http_method_names = ['post']

class PATCHTareaView(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = PATCHTareaRequest
    http_method_names = ['patch']
    

class DELETETareaView(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = DELETETareaRequest
    http_method_names = ['delete']