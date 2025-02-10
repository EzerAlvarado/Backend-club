from rest_framework import serializers
from club.models import Cargo

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'total_cobro', 'fecha_cobro', 'usuario_responsable', 'estado', 'mesa']
