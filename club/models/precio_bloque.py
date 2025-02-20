from django.db import models

class PrecioBloque(models.Model):
    """
    Modelo de PrecioBloques
    """  
    precio_actual = models.DecimalField(max_digits=18,
                                        null=True,
                                        blank=True,
                                        help_text='Precio actual del bloque',
                                        decimal_places=2)
    
    ultima_actualizacion = models.DateTimeField(null=True,
                                blank=True,
                                help_text='Fecha de la ultima actualizacion')

    class Meta:
        db_table = 'precio_bloque'
        ordering = ['pk']
        verbose_name = 'Precio Bloque'
        verbose_name_plural = 'Precio Bloques'
        permissions = [
            ['autorizar_precio_bloque', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_precio_bloque', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Precio Del Bloque: {self.precio_actual} | Fecha: {self.ultima_actualizacion} "

