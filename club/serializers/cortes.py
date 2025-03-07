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
        fields = '__all__'
        read_only_fields = ('id',)