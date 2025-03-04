"""Usuario filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Usuario


class UsuarioFilter(filters.FilterSet):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'estado_solicitud',
            'nombre',
            'eliminado',
            'numero_de_celular',
            'correo_cliente',
        )        