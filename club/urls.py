from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('bloques', views.BloqueViewSet)
router.register('clientes', views.ClienteViewSet)
router.register('cortes', views.CorteViewSet)
router.register('eventos', views.EventoViewSet)
router.register('ganancias', views.GananciaViewSet)
router.register('mesas', views.MesaViewSet)
router.register('ordenes-de-compra', views.OrdenDeCompraViewSet)
router.register('precio-bloque', views.PrecioBloqueViewSet)
router.register('productos', views.ProductoViewSet)
router.register('tickets', views.TicketViewSet)
router.register('usuarios', views.UsuarioViewSet)
router.register('cargos', views.CargoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ordenes/crear/', views.OrdenDeCompraViewSet.as_view({'post': 'crear_orden'}), name='crear_orden'),
    path('cargos/<int:pk>/pagar/', views.CargoViewSet.as_view({'post': 'pagar'}), name='pagar_cargo'),
]
