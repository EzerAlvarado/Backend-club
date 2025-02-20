from rest_framework import viewsets
from club.models import Cargo
from club.serializers.cargos import CargoSerializer
from club.filters.cargos import CargoFilter
import django_filters.rest_framework as filters

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filterset_class = CargoFilter