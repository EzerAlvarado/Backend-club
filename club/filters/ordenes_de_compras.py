"""OrdenDeCompra filters."""

# utilities
import django_filters
from django_filters import rest_framework as filters

# Models
from club.models import OrdenDeCompra

class OrdenDeCompraFilter(filters.FilterSet):
    fecha_de_orden = django_filters.DateFromToRangeFilter()
    precio_orden = django_filters.RangeFilter()
    cantidad = django_filters.RangeFilter()
    
    class Meta:
        model = OrdenDeCompra
        fields = ['id', 'cantidad', 'fecha_de_orden', 'precio_orden', 'mesa', 'nota', 'producto', 'listo_a_pagar', 'usuario_responsable', 'estado']
