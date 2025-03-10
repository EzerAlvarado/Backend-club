from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from club.models import Cargo
from club.serializers.cargos import CargoSerializer
from club.serializers.tickets import TicketModelSerializer
from club.serializers.tickets_preview import TicketProvisionalSerializer
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

    @action(detail=False, methods=['get'])
    def ticket_provisional(self, request):
        """
        Obtiene el ticket provisional de una mesa con su cargo pendiente.
        """
        mesa_id = request.query_params.get('mesa_id')

        if not mesa_id:
            return Response({'error': 'Se requiere mesa_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            mesa_id = int(mesa_id)
            cargos = Cargo.objects.filter(mesa_id=mesa_id, estado='pendiente')

            if not cargos.exists():
                return Response({'error': 'No hay un cargo pendiente para esta mesa'}, status=status.HTTP_404_NOT_FOUND)

            serializer = TicketProvisionalSerializer(cargos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'mesa_id debe ser un número válido'}, status=status.HTTP_400_BAD_REQUEST)
