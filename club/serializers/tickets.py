"""Ticket serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Ticket

class TicketModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Ticket
    """

    class Meta:
        model = Ticket
        fields = (
            'id',
            'cantidad',
            'cargo',
            'fecha_de_orden',
        )        
        read_only_fields = ('id',)