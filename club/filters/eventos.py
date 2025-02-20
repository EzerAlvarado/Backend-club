"""Evento filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Evento


class EventoFilter(filters.FilterSet):
    class Meta:
        model = Evento
        fields = (
            'id',
            'pago_renta',
            'fecha_inicio_de_evento',
            'fecha_final_de_evento',
            'observaciones',
            'bloque',
            'cliente_rentador',
        )        