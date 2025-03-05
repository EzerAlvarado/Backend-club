from django.contrib import admin

# Register your models here.
from club import models


admin.site.register(models.Bloque)
admin.site.register(models.Cliente)
admin.site.register(models.Corte)
admin.site.register(models.Evento)
admin.site.register(models.Ganancia)
admin.site.register(models.Inventario)
admin.site.register(models.Mesa)
admin.site.register(models.OrdenDeCompra)
admin.site.register(models.Producto)
admin.site.register(models.Ticket)
admin.site.register(models.Usuario)
admin.site.register(models.Producto)
admin.site.register(models.PrecioBloque)
admin.site.register(models.Cargo)