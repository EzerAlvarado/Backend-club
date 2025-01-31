from django.shortcuts import render

# Create your views here.
#models
from club.models import Ganancia
#rest
from rest_framework import viewsets
#utilities
from club.serializers.ganancias import GananciaModelSerializer
#filters
from club.filters.ganancias import GananciaFilter

class GananciaViewSet(viewsets.ModelViewSet):
    """
    View de Ganancias
    Maneja CRUD
    """
    queryset=Ganancia.objects.all()
    serializer_class = GananciaModelSerializer
    filterset_class = GananciaFilter
