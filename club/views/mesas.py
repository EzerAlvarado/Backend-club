from django.shortcuts import render

# Create your views here.
#models
from club.models import Mesa
#rest
from rest_framework import viewsets
#utilities
from club.serializers.mesas import MesaModelSerializer
#filters
from club.filters.mesas import MesaFilter

class MesaViewSet(viewsets.ModelViewSet):
    """
    View de Mesas
    Maneja CRUD
    """
    queryset=Mesa.objects.all()
    serializer_class = MesaModelSerializer
    filterset_class = MesaFilter
