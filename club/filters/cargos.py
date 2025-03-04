import django_filters
from club.models import Cargo

class CargoFilter(django_filters.FilterSet):
    # Filtros por estado y fecha de cobro
    estado = django_filters.ChoiceFilter(choices=Cargo.ESTADO_CHOICES)
    fecha_cobro = django_filters.DateFromToRangeFilter(field_name='fecha_cobro')

    class Meta:
        model = Cargo
        fields = ['estado', 'fecha_cobro', 'usuario_responsable', 'nota','mesa']
