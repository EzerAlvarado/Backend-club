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
            'precio_orden',
            'mesas',
            'nota',
            'producto',
            'listo_a_pagar',
            'usuario_responsable',
        )        