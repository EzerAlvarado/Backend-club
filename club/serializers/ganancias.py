"""Ganancia serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Ganancia

class GananciaModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Ganancia
    """

    class Meta:
        model = Ganancia
        fields = (
            'id',
            'total',
            'fecha',
        )        
        read_only_fields = ('id',)