from django.shortcuts import render

# Create your views here.
#models
from club.models import Bloque
#rest
from rest_framework import viewsets
#utilities
from club.serializers.bloques import BloqueModelSerializer
#filters
from club.filters.bloques import BloqueFilter

class BloqueViewSet(viewsets.ModelViewSet):
    """
    View de Bloques
    Maneja CRUD
    """
    queryset=Bloque.objects.all()
    serializer_class = BloqueModelSerializer
    filterset_class = BloqueFilter
