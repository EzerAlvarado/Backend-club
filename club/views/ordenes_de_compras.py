from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from collections import defaultdict
from club.models import Mesa, Producto, OrdenDeCompra, Usuario
from club.serializers.ordenes_de_compras import OrdenDeCompraModelSerializer
from club.serializers.services import crear_orden

class OrdenDeCompraViewSet(viewsets.ModelViewSet):
    queryset = OrdenDeCompra.objects.all()
    serializer_class = OrdenDeCompraModelSerializer
    
    def list(self, request, *args, **kwargs):
        """
        Retorna las órdenes de compra agrupadas por mesa.
        """
        ordenes = self.get_queryset().filter(listo_a_pagar=False)
        data_agrupada = defaultdict(list)

        for orden in ordenes:
            data_agrupada[orden.mesa_id].append(OrdenDeCompraModelSerializer(orden).data)

        return Response(data_agrupada)

    @action(detail=False, methods=['post'])
    def crear_orden(self, request):
        """
        Endpoint para crear una orden y actualizar el cargo automáticamente.
        """
        mesa_id = request.data.get('mesa_id')
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad')
        nota = request.data.get('nota')
        usuario_responsable_id = request.data.get('usuario_responsable_id') 
        
        if not mesa_id or not producto_id or not cantidad or not usuario_responsable_id:
            return Response({'error': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            mesa = Mesa.objects.get(id=mesa_id)
            producto = Producto.objects.get(id=producto_id)
            usuario_responsable = Usuario.objects.get(id=usuario_responsable_id)

            orden = crear_orden(mesa, producto, int(cantidad), usuario_responsable, nota)

            return Response(OrdenDeCompraModelSerializer(orden).data, status=status.HTTP_201_CREATED)
        
        except Mesa.DoesNotExist:
            return Response({'error': 'Mesa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario responsable no encontrado'}, status=status.HTTP_404_NOT_FOUND)