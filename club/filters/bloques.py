"""Bloque filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Bloque


class BloqueFilter(filters.FilterSet):
    class Meta:
        model = Bloque
        fields = (
            'id',
            'descripcion',
            'disponibilidad',
            'mesas',
            'precio_bloque',
            'en_donde_es_rentado',
        )        