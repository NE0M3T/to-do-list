from rest_framework import viewsets
from .models import Tarea
from .serializer import TareaSerializer

# Create your views here.

class TareaView(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer