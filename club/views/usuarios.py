from django.shortcuts import render

# Create your views here.
#models
from club.models import Usuario
#rest
from rest_framework import viewsets
#utilities
from club.serializers.usuarios import UsuarioModelSerializer
#filters
from club.filters.usuarios import UsuarioFilter

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    View de Usuarios
    Maneja CRUD
    """
    queryset=Usuario.objects.all()
    serializer_class = UsuarioModelSerializer
    filterset_class = UsuarioFilter
