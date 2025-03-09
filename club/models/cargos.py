from django.db import models

class Cargo(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    ]
    total_cobro = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_cobro = models.DateTimeField(null=True, blank=False)
    nota = models.TextField(null=True, blank=True)
    usuario_responsable = models.ForeignKey('club.Usuario', on_delete=models.DO_NOTHING)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    mesa = models.ForeignKey('club.Mesa', on_delete=models.DO_NOTHING) 

    class Meta:
        db_table = 'cargos'
        ordering = ['pk']
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        permissions = [
            ['autorizar_cargo', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_cargo', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Cargo {self.id} - {self.estado}"