"""Bloque serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Bloque

class BloqueModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Bloque
    """

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
        read_only_fields = ('id',)