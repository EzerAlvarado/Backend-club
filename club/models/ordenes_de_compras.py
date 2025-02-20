from django.db import models

class OrdenDeCompra(models.Model):
    """
    Modelo de Ordenes de compras
    """ 
    completado = models.BooleanField(default=False)
    
    listo_a_pagar = models.BooleanField(default=False)
    
    precio_orden = models.DecimalField(max_digits=10, decimal_places=2,
                                        null=True,
                                        blank=False)
    
    cantidad = models.IntegerField(null=False,
                                   blank=False,
                                   help_text='cantidad de producto solicitado')

    fecha_de_orden = models.DateField(null=False,
                                      blank=False,
                                      help_text='fecha de la orden de compra')
    
    mesas = models.ForeignKey("club.Mesa",
                              null=False,
                              blank=False,
                              related_name='ordenes_de_compras',
                              help_text='Relacion a la mesa donde se hizo la orden',
                              on_delete=models.DO_NOTHING)
    
    producto = models.ForeignKey("club.Producto",
                                 null=False,
                                 blank=False,
                                 related_name='ordenes_de_compras',
                                 help_text='Relacion del producto que se ordeno',
                                 on_delete=models.DO_NOTHING)
    
    cargo = models.ForeignKey("club.Cargo",
                            null=True,
                            blank=False,
                            related_name='ordenes_de_compras',
                            help_text='Relacion al cargo',
                            on_delete=models.DO_NOTHING)

    usuario_responsable = models.ForeignKey("club.Usuario",
                                            null=False,
                                            blank=False,
                                            related_name='ordenes_de_compras',
                                            help_text='Relacion del usuario que hizo la orden',
                                            on_delete=models.DO_NOTHING)

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
        return f"Pk: {self.pk} | Cantidad: {self.cantidad} | Fecha: {self.fecha_de_orden} "

