from django.db import models

class Evento(models.Model):
    """
    Modelo de eventos
    """
    nombre_rentador = models.CharField(max_length=200,
                              null=True,
                              blank=True,
                              help_text='Nombre del cliente que renta')
    
    correo_rentador = models.CharField(max_length=150,
                                      null=True,
                                      blank=True,
                                      help_text='Correo del cliente que renta')
    
    pago_renta = models.BooleanField(default=True)
    
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
    bloque = models.ManyToManyField("club.Bloque",
                                    related_name='bloques',
                                    help_text='Relacion al bloque donde esta el evento')

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
