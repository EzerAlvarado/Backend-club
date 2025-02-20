"""PrecioBloque serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import PrecioBloque

class PrecioBloqueModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un PrecioBloque
    """

    class Meta:
        model = PrecioBloque
        fields = (
            'id',
            'precio_actual',
            'ultima_actualizacion',
        )        
        read_only_fields = ('id',)