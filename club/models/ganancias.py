from django.db import models

class Ganancia(models.Model):
    """
    Modelo de Ganancias
    """  
    total = models.DecimalField(max_digits=18,
                                null=True,
                                blank=True,
                                help_text='Total de ganancias diarias',
                                decimal_places=2)
    
    fecha = models.DateField(null=True,
                            blank=True,
                            help_text='Fecha del dia de la ganacia')

    class Meta:
        db_table = 'ganancia'
        ordering = ['pk']
        verbose_name = 'Ganancia'
        verbose_name_plural = 'Ganancias'
        permissions = [
            ['autorizar_ganancia', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_ganancia', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Total Ganancia: {self.total} | Fecha: {self.fecha} "

