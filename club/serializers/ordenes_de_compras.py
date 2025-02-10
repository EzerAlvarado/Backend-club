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
        fields = (
            'id',
            'cantidad',
            'fecha_de_orden',
            'completado',
            'mesas',
            'precio_orden',
            'cargo',
            'listo_a_pagar',
            'producto',
            'nombre_producto', 
            'usuario_responsable',
        )

    def get_nombre_producto(self, obj):
        return obj.producto.nombre_producto if obj.producto else None