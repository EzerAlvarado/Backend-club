from django.shortcuts import render

# Create your views here.
#models
from club.models import OrdenDeCompra
#rest
from rest_framework import viewsets
#utilities
from club.serializers.ordenes_de_compras import OrdenDeCompraModelSerializer
#filters
from club.filters.ordenes_de_compras import OrdenDeCompraFilter

class OrdenDeCompraViewSet(viewsets.ModelViewSet):
    """
    View de OrdenDeCompras
    Maneja CRUD
    """
    queryset=OrdenDeCompra.objects.all()
    serializer_class = OrdenDeCompraModelSerializer
    filterset_class = OrdenDeCompraFilter
