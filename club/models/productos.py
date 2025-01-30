from django.db import models

class Producto(models.Model):
    """
    Modelo de Productos
    """  
    nombre_producto = models.CharField(max_length=150,
                                       null=False,
                                       blank=False,
                                       help_text='Nombre del producto')
    
    categoria = models.CharField(max_length=100,
                                 null=False,
                                 blank=False,
                                 help_text='Categoria del producto si es, Vino, Cerveza, Etc')

    class Meta:
        db_table = 'productos'
        ordering = ['pk']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        permissions = [
            ['autorizar_producto', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_producto', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]

    def __str__(self):
        return f"Pk: {self.pk} | Nombre Producto: {self.nombre_producto} | Categoria: {self.categoria} "

