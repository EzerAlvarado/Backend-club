from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from club.models import Cargo
from club.serializers.cargos import CargoSerializer
from club.serializers.tickets import TicketModelSerializer
from club.filters.cargos import CargoFilter
from club.serializers.services import pagar_cargo


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filterset_class = CargoFilter

    @action(detail=True, methods=['post'])
    def pagar(self, request, pk=None):
        """
        Endpoint para pagar un cargo y generar un ticket.
        """
        try:
            cargo = Cargo.objects.get(id=pk, estado='pendiente')
            ticket = pagar_cargo(cargo)
            return Response(TicketModelSerializer(ticket).data, status=status.HTTP_200_OK)
        except Cargo.DoesNotExist:
            return Response({'error': 'Cargo no encontrado o ya pagado'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
