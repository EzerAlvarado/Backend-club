from django.shortcuts import render

# Create your views here.
#models
from club.models import PrecioBloque
#rest
from rest_framework import viewsets
#utilities
from club.serializers.precio_bloque import PrecioBloqueModelSerializer
#filters
from club.filters.precio_bloque import PrecioBloqueFilter

class PrecioBloqueViewSet(viewsets.ModelViewSet):
    """
    View de PrecioBloques
    Maneja CRUD
    """
    queryset=PrecioBloque.objects.all()
    serializer_class = PrecioBloqueModelSerializer
    filterset_class = PrecioBloqueFilter
