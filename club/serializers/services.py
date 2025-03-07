from club.models import OrdenDeCompra, Cargo, Ticket
from django.db import transaction

def crear_orden(mesa, producto, cantidad):
    """
    Crea una nueva orden de compra para una mesa y actualiza el cargo correspondiente.
    """
    with transaction.atomic():
        orden = OrdenDeCompra.objects.create(
            mesa=mesa, 
            producto=producto, 
            cantidad=cantidad,
            estado='pendiente'
        )
        
        # Buscar si ya existe un cargo para la mesa
        cargo, creado = Cargo.objects.get_or_create(mesa=mesa, pagado=False)
        
        # Sumar el total de la nueva orden al cargo
        cargo.total += producto.precio * cantidad
        cargo.save()
        
        # Marcar la orden como incluida en el cargo
        orden.estado = 'incluido_en_cargo'
        orden.save()

        return orden


def pagar_cargo(cargo):
    """
    Paga un cargo y genera un ticket asociado.
    """
    if cargo.pagado:
        raise ValueError("Este cargo ya está pagado.")

    with transaction.atomic():
        # Marcar el cargo como pagado
        cargo.pagado = True
        cargo.save()

        # Crear un ticket con el total pagado
        ticket = Ticket.objects.create(
            cargo=cargo,
            total_pagado=cargo.total
        )

        return ticket
