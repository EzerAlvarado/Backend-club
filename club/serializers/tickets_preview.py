from rest_framework import serializers
from club.models import Cargo, OrdenDeCompra

class TicketProvisionalSerializer(serializers.ModelSerializer):
    productos = serializers.SerializerMethodField()
    total_cobro = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Cargo
        fields = ['mesa', 'productos', 'total_cobro']

    def get_productos(self, obj):
        """
        Obtiene los productos del cargo pendiente junto con la cantidad y subtotal.
        """
        ordenes = OrdenDeCompra.objects.filter(mesa=obj.mesa, estado='incluido_en_cargo')
        productos_data = []

        for orden in ordenes:
            productos_data.append({
                'producto': orden.producto.nombre_producto,
                'cantidad': orden.cantidad,
                'precio_unitario': orden.producto.precio,
                'subtotal': orden.cantidad * orden.producto.precio
            })
        
        return productos_data
