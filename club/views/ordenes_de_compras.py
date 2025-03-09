from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from club.models import Mesa, Producto, OrdenDeCompra
from club.serializers.ordenes_de_compras import  OrdenDeCompraModelSerializer
from club.serializers.services import crear_orden, pagar_cargo

class OrdenDeCompraViewSet(viewsets.ModelViewSet):
    queryset = OrdenDeCompra.objects.all()
    serializer_class = OrdenDeCompraModelSerializer

    @action(detail=False, methods=['post'])
    def crear_orden(self, request):
        """
        Endpoint para crear una orden y actualizar el cargo automáticamente.
        """
        mesa_id = request.data.get('mesa_id')
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad')

        if not mesa_id or not producto_id or not cantidad:
            return Response({'error': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            mesa = Mesa.objects.get(id=mesa_id)
            producto = Producto.objects.get(id=producto_id)
            orden = crear_orden(mesa, producto, int(cantidad))
            return Response(OrdenDeCompraModelSerializer(orden).data, status=status.HTTP_201_CREATED)
        except Mesa.DoesNotExist:
            return Response({'error': 'Mesa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
