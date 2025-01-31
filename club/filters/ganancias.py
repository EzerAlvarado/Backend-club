"""Ganancia filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Ganancia


class GananciaFilter(filters.FilterSet):
    class Meta:
        model = Ganancia
        fields = (
            'id',
            'total',
            'fecha',
        )        