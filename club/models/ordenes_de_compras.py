from django.db import models

class OrdenDeCompra(models.Model):
    ESTADO_ORDEN = [
        ('pendiente', 'Pendiente'),
        ('incluido_en_cargo', 'Incluido en Cargo'),
        ('cancelado', 'Cancelado'),
    ]

    estado = models.CharField(max_length=20, choices=ESTADO_ORDEN, default='pendiente')
    listo_a_pagar = models.BooleanField(default=False)
    precio_orden = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    cantidad = models.IntegerField(null=False, blank=False, help_text='Cantidad de producto solicitado')
    fecha_de_orden = models.DateField(auto_now_add=True, null=False, blank=False, help_text='Fecha de la orden de compra')
    
    mesa = models.ForeignKey("club.Mesa", null=True, blank=True, related_name='ordenes_de_compras', on_delete=models.DO_NOTHING)
    producto = models.ForeignKey("club.Producto", null=True, blank=True, related_name='ordenes_de_compras', on_delete=models.DO_NOTHING)
    nota = models.TextField(null=True, blank=True)
    
    cargo = models.ForeignKey("club.Cargo", null=True, blank=True, related_name='ordenes_de_compras', on_delete=models.DO_NOTHING)
    usuario_responsable = models.ForeignKey("club.Usuario",  null=False, blank=False, related_name='ordenes_de_compras', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'ordenes_de_compras'
        ordering = ['pk']
        verbose_name = 'Orden De Compra'
        verbose_name_plural = 'Ordenes De Compras'
        permissions = [
            ['autorizar_ordencompra', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_ordencompra', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Cantidad: {self.cantidad} | Fecha: {self.fecha_de_orden} | Estado: {self.estado}"
