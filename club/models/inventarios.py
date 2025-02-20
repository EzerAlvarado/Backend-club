from django.db import models

class Inventario(models.Model):
    """
    Modelo de Inventarios
    """  
    tipo_de_movimiento = models.CharField(max_length=50,
                                          null=True,
                                          blank=True,
                                          help_text='Tipo de movimiento si fue adquisicion de producto, venta, etc')
    
    fecha_movimiento = models.DateTimeField(null=True,
                                            blank=True,
                                            help_text='Fecha y hora del movimiento')

    observaciones = models.TextField(null=True,
                                     blank=True,
                                     help_text='Observaciones del inventario')

    cantidad = models.IntegerField(null=False,
                                   blank=False,
                                   help_text='Cantidad del producto relacionado')
    
    producto_id: int
    producto = models.ForeignKey("club.Producto",
                                 null=False,
                                 blank=False,
                                 related_name='inventarios',
                                 help_text='Relacion al Producto que esta en el inventario',
                                 on_delete=models.DO_NOTHING)
    
    #TODO: RElacion a usuario
    # usuario_responsable_id: int
    # usuario_responsable = models.ForeignKey("club.Usuario",
    #                                         null=False,
    #                                         blank=False,
    #                                         related_name='inventarios',
    #                                         help_text='Relacion a Usuario Responsable',
    #                                         on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'inventarios'
        ordering = ['pk']
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        permissions = [
            ['autorizar_inventario', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_inventario', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Cantidad producto: {self.cantidad} | Producto: {self.producto} "

