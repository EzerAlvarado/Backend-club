from django.db import models

class Corte(models.Model):
    """
    Modelo de Cortes
    """  
    fecha_apertura = models.DateTimeField(null=False,
                                            blank=False,
                                            help_text='Fecha de apertura del corte')
                                            
    fecha_cierre = models.DateTimeField(null=True,
                                        blank=True,
                                        help_text='Fecha de cierre del corte')

    dinero_caja_inicio = models.DecimalField(max_digits=18,
                                            null=True,
                                            blank=True,
                                            help_text='Dinero con el que se cuenta al inciar corte',
                                            decimal_places=2)
    
    dinero_caja_fin = models.DecimalField(max_digits=18,
                                            null=True,
                                            blank=True,
                                            help_text='Dinero con el que se cuenta al finalizar corte',
                                            decimal_places=2)
    
    observaciones = models.TextField(null=True,
                                     blank=True,
                                     help_text='Observaciones del corte')
    
    #TODO: Relacion Usuario
    # usuario_responsable_id: int
    # usuario_responsable = models.ForeignKey("club.Usuario", 
    #                                         null=False,
    #                                         blank=False,
    #                                         related_name='cortes',
    #                                         help_text='',
    #                                         on_delete=models.DO_NOTHING)

    
    class Meta:
        db_table = 'cortes'
        ordering = ['pk']
        verbose_name = 'Corte'
        verbose_name_plural = 'Cortes'
        permissions = [
            ['autorizar_corte', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_corte', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Fecha Apertura: {self.fecha_apertura} | Fecha Cierre: {self.fecha_cierre} "

