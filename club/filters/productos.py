"""Producto filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Producto


class ProductoFilter(filters.FilterSet):
    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre_producto',
            'precio',
            'categoria',
        )        