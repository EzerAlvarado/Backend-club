from django.db import models

class Bloque(models.Model):
    """
    Modelo de Bloques
    """  
    descripcion = models.CharField(max_length=50,
                                   null=False,
                                   blank=False,
                                   help_text='Seccion donde esta el bloque, ej Bloque A, B, etc')

    disponibilidad = models.BooleanField(default=True)
    
    mesas_id: int
    mesas = models.ManyToManyField("club.Mesas",
                                   related_name='bloques',
                                   help_text='Relacion a las mesas que son del bloque')

    en_donde_es_rentado_id: int
    en_donde_es_rentado = models.ForeignKey("club.Evento",
                                            null=True,
                                            blank=True,
                                            help_text='Relacion si disponibilidad es False, esta relacion indicara donde es rentado',
                                            related_name='bloques',
                                            on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'bloques'
        ordering = ['pk']
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'
        permissions = [
            ['autorizar_bloque', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_bloque', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Descripcion: {self.descripcion} | Disponibilidad: {self.disponibilidad} "
