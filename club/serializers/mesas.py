"""Mesa serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Mesa

class MesaModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Mesa
    """

    class Meta:
        model = Mesa
        fields = (
            'id',
            'descripcion',
            'capacidad_personas',
            'esta_disponible',
        )        
        read_only_fields = ('id',)