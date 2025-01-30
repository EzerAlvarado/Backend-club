from django.db import models

class Ticket(models.Model):
    """
    Modelo de Tickets
    """  
    total = models.DecimalField(max_digits=18,
                                null=True,
                                blank=True,
                                help_text='Total de ganancias diarias',
                                decimal_places=2)
    
    fecha = models.DateTimeField(null=True,
                                blank=True,
                                help_text='Fecha del dia de la ganacia')

    class Meta:
        db_table = 'tickets'
        ordering = ['pk']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        permissions = [
            ['autorizar_tickets', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_tickets', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Total Ganancia: {self.total} | Fecha: {self.fecha} "

