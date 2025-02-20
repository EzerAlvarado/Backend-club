from django.shortcuts import render

# Create your views here.
#models
from club.models import Corte
#rest
from rest_framework import viewsets
#utilities
from club.serializers.cortes import CorteModelSerializer
#filters
from club.filters.cortes import CorteFilter

class CorteViewSet(viewsets.ModelViewSet):
    """
    View de Cortes
    Maneja CRUD
    """
    queryset=Corte.objects.all()
    serializer_class = CorteModelSerializer
    filterset_class = CorteFilter
