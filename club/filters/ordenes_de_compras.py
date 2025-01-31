"""OrdenDeCompra filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import OrdenDeCompra


class OrdenDeCompraFilter(filters.FilterSet):
    class Meta:
        model = OrdenDeCompra
        fields = (
            'id',
            'cantidad',
            'fecha_de_orden',
            'OrdenDeCompras',
            'producto',
            'usuario_responsable',
        )        