"""Usuario serializers."""

# Django
from django.db.models import Q

# Django REST Framework
from rest_framework import serializers

# Models
from club.models import Usuario

class UsuarioModelSerializer(serializers.ModelSerializer):
    """
        serializer para crear, editar, obtener y eliminar
        a un Usuario
    """

    class Meta:
        model = Usuario
        fields = (
            'id',
            'estado_solicitud',
            'nombre',
            'numero_de_celular',
            'correo_cliente',
            'contrasena',
        )        
        read_only_fields = ('id',)