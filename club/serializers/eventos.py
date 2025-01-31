"""Evento serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Evento

class EventoModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Evento
    """

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
        read_only_fields = ('id',)