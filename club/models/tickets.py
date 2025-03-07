from django.db import models

class Ticket(models.Model):
    total = models.DecimalField(null=True,max_digits=18, decimal_places=2, default=0.00, help_text='Total de ganancias diarias')
    fecha = models.DateTimeField(null=True, auto_now_add=True, help_text='Fecha del día de la ganancia')
    cargo = models.ForeignKey("club.Cargo", null=True, blank=False, related_name='tickets', on_delete=models.DO_NOTHING)

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
        return f"Pk: {self.pk} | Total Ganancia: {self.total} | Fecha: {self.fecha}"
