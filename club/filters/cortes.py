"""Corte filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Corte


class CorteFilter(filters.FilterSet):
    class Meta:
        model = Corte
        fields = (
            'id',
            'fecha_apertura',
            'fecha_cierre',
            'dinero_caja_inicio',
            'dinero_caja_fin',
            'observaciones',
        )        