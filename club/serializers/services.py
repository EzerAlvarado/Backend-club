from club.models import OrdenDeCompra, Cargo, Ticket
from django.db import transaction
from django.utils import timezone
from decimal import Decimal

def crear_orden(mesa, producto, cantidad, usuario_responsable, nota):
    """
    Crea una nueva orden de compra para una mesa y actualiza el cargo correspondiente.
    """
    with transaction.atomic():
        orden = OrdenDeCompra.objects.create(
            mesa=mesa, 
            producto=producto, 
            cantidad=cantidad,
            usuario_responsable=usuario_responsable,
            nota=nota,
            fecha_de_orden=timezone.now(),
            estado='pendiente'
        )
        
        cargo, creado = Cargo.objects.get_or_create(mesa=mesa, estado='pendiente',usuario_responsable=usuario_responsable)
        
        cargo.total_cobro = Decimal(cargo.total_cobro)  

        cargo.total_cobro += Decimal(producto.precio) * Decimal(cantidad)
        cargo.save()

        orden.estado = 'incluido_en_cargo'
        orden.save()

        return orden


def pagar_cargo(cargo):
    """
    Paga un cargo y genera un ticket asociado.
    """
    if cargo.estado == 'pagado':
        raise ValueError("Este cargo ya está pagado.")

    with transaction.atomic():
        cargo.estado = 'pagado'
        cargo.fecha_cobro = timezone.now()  
        cargo.save()

        ticket = Ticket.objects.create(
            cargo=cargo,
            total=cargo.total_cobro
        )

        return ticket
