"""Cliente filters."""

# utilities
from django_filters import rest_framework as filters

# Models
from club.models import Cliente


class ClienteFilter(filters.FilterSet):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'nombre',
            'tipo_de_cliente',
            'numero_de_celular',
            'correo_cliente',
        )        