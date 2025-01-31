"""Producto serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Producto

class ProductoModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Producto
    """

    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre_producto',
            'categoria',
        )        
        read_only_fields = ('id',)