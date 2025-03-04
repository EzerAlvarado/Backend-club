from django.db import models

class Usuario(models.Model):
    """
    Modelo de Usuario
    """  
    
    OPCIONES_USUARIO = [
        ('M', 'Mesero'),
        ('C', 'Caja'),
        ('B', 'Bartender'),
    ]    
    estado_solicitud =  models.CharField(max_length=1,choices=OPCIONES_USUARIO,)
    
    nombre = models.CharField(max_length=200,
                              null=False,
                              blank=False,
                              help_text='Nombre del cliente')

    numero_de_celular = models.BigIntegerField(null=True,
                                               blank=True,
                                               help_text='Numero de telefono del cliente')
    
    correo_cliente = models.CharField(max_length=150,
                                      null=True,
                                      blank=True,
                                      help_text='Correo del cliente')
    
    eliminado = models.BooleanField(default=False,
                                    help_text='Bandera para dar de baja un usuario')

    class Meta:
        db_table = 'usuario'
        ordering = ['pk']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        permissions = [
            ['autorizar_usuario', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_usuario', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Cliente: {self.nombre} | Tipo De Cliente: {self.tipo_de_cliente} "

