"""Corte serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Corte

class CorteModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Corte
    """

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
        read_only_fields = ('id',)