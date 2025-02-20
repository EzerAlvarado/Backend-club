from django.db import models

class Cliente(models.Model):
    """
    Modelo de Clientes
    """  
    nombre = models.CharField(max_length=200,
                              null=False,
                              blank=False,
                              help_text='Nombre del cliente')
    
    tipo_de_cliente =models.CharField(max_length=50,
                                      null=False,
                                      blank=False,
                                      help_text='Tipo de cliente Vip, Frecuente, Nuevo, etc')

    numero_de_celular = models.BigIntegerField(null=True,
                                               blank=True,
                                               help_text='Numero de telefono del cliente')
    
    correo_cliente = models.CharField(max_length=150,
                                      null=True,
                                      blank=True,
                                      help_text='Correo del cliente')

    class Meta:
        db_table = 'clientes'
        ordering = ['pk']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        permissions = [
            ['autorizar_cliente', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_cliente', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Cliente: {self.nombre} | Tipo De Cliente: {self.tipo_de_cliente} "

