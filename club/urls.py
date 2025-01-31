from django.urls import path,include
from rest_framework import routers
from club import views


router = routers.DefaultRouter()
router.register('bloques',views.BloqueViewSet)
router.register('clientes',views.ClienteViewSet)
router.register('cortes',views.CorteViewSet)
router.register('eventos',views.EventoViewSet)
router.register('ganancias',views.GananciaViewSet)
router.register('mesas',views.MesaViewSet)
router.register('ordenes-de-compra',views.OrdenDeCompraViewSet)
router.register('precio-bloque',views.PrecioBloqueViewSet)
router.register('productos',views.ProductoViewSet)
router.register('tickets',views.TicketViewSet)
router.register('usuarios',views.UsuarioViewSet)


urlpatterns=[
    path('', include(router.urls))
]