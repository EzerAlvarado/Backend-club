"""Mesa filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Mesa


class MesaFilter(filters.FilterSet):
    class Meta:
        model = Mesa
        fields = (
            'id',
            'descripcion',
            'esta_disponible',
        )        