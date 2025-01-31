from django.shortcuts import render

# Create your views here.
#models
from club.models import Producto
#rest
from rest_framework import viewsets
#utilities
from club.serializers.productos import ProductoModelSerializer
#filters
from club.filters.productos import ProductoFilter

class ProductoViewSet(viewsets.ModelViewSet):
    """
    View de Productos
    Maneja CRUD
    """
    queryset=Producto.objects.all()
    serializer_class = ProductoModelSerializer
    filterset_class = ProductoFilter
