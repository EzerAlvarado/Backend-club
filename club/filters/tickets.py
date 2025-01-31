"""Ticket filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Ticket


class TicketFilter(filters.FilterSet):
    class Meta:
        model = Ticket
        fields = (
            'id',
            'cantidad',
            'fecha_de_orden',
        )        