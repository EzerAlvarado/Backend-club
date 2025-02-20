"""Cliente serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Cliente

class ClienteModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Cliente
    """

    class Meta:
        model = Cliente
        fields = (
            'id',
            'nombre',
            'tipo_de_cliente',
            'numero_de_celular',
            'correo_cliente',
        )        
        read_only_fields = ('id',)