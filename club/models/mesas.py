from django.db import models

class Mesa(models.Model):
    """
    Modelo de Bloques
    """  
    descripcion = models.CharField(max_length=50,
                                   null=False,
                                   blank=False,
                                   help_text='Tipo de mesa')

    capacidad_personas = models.IntegerField(null=False,
                                             blank=False,
                                             help_text='Capacidad de personas que permite la mesa')
    
    esta_disponible = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'mesas'
        ordering = ['pk']
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
        permissions = [
            ['autorizar_mesa', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_mesa', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Descripcion: {self.descripcion} | Capacidad: {self.capacidad_personas} "

