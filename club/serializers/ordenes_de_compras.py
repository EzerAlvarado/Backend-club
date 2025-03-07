"""OrdenDeCompra serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import OrdenDeCompra


class OrdenDeCompraModelSerializer(serializers.ModelSerializer):
    nombre_producto = serializers.SerializerMethodField()

    class Meta:
        model = OrdenDeCompra
        fields = '__all__'

    def get_nombre_producto(self, obj):
        return obj.producto.nombre_producto if obj.producto else None