"""OrdenDeCompra serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import OrdenDeCompra

class OrdenDeCompraModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un OrdenDeCompra
    """

    class Meta:
        model = OrdenDeCompra
        fields = (
            'id',
            'cantidad',
            'fecha_de_orden',
            'mesas',
            'producto',
            'usuario_responsable',
        )        
        read_only_fields = ('id',)