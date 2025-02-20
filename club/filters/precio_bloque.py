"""PrecioBloque filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import PrecioBloque


class PrecioBloqueFilter(filters.FilterSet):
    class Meta:
        model = PrecioBloque
        fields = (
            'id',
            'precio_actual',
            'ultima_actualizacion',
        )        