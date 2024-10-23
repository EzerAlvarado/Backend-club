from django.db import models

class Evento(models.Model):
    """
    Modelo de eventos
    """  
    pago_renta = models.BooleanField(default=False)
    
    fecha_inicio_de_evento = models.DateTimeField(null=True, 
                                                blank=True, 
                                                help_text='Indica la fecha inicio del evento')
    
    fecha_final_de_evento = models.DateTimeField(null=True, 
                                                blank=True, 
                                                help_text='Indica la fecha fin del evento')
    
    observaciones = models.TextField(null=True, 
                                    blank=True, 
                                    help_text='Indica cualquier información referente al evento')
    
    bloque_id: int
    bloque = models.ForeignKey("club.Bloque",
                               null=False,
                               blank=False,
                               related_name='bloques',
                               help_text='Relacion al bloque donde esta el evento',
                               on_delete=models.DO_NOTHING)
    
    precio_bloque_id: int
    precio_bloque = models.ForeignKey("club.PrecioBloque",
                                      null=False,
                                      blank=False,
                                      related_name='bloques',
                                      help_text='Relacion al precio del bloque en cuestion',
                                      on_delete=models.DO_NOTHING)
    
    cliente_rentador_id: int
    cliente_rentador = models.ForeignKey("club.ClienteRentador",
                                      null=False,
                                      blank=False,
                                      related_name='bloques',
                                      help_text='Relacion al cliente que renta',
                                      on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'eventos'
        ordering = ['pk']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        permissions = [
            ['autorizar_evento', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_evento', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Fecha Inicio: {self.fecha_inicio_de_evento} | Fecha Fin: {self.fecha_final_de_evento}"
