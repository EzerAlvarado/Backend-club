from django.shortcuts import render

# Create your views here.
#models
from club.models import Cliente
#rest
from rest_framework import viewsets
#utilities
from club.serializers.clientes import ClienteModelSerializer
#filters
from club.filters.clientes import ClienteFilter

class ClienteViewSet(viewsets.ModelViewSet):
    """
    View de Clientes
    Maneja CRUD
    """
    queryset=Cliente.objects.all()
    serializer_class = ClienteModelSerializer
    filterset_class = ClienteFilter
