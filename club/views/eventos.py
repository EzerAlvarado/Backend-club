from django.shortcuts import render

# Create your views here.
#models
from club.models import Evento
#rest
from rest_framework import viewsets
#utilities
from club.serializers.eventos import EventoModelSerializer
#filters
from club.filters.eventos import EventoFilter

class EventoViewSet(viewsets.ModelViewSet):
    """
    View de Eventos
    Maneja CRUD
    """
    queryset=Evento.objects.all()
    serializer_class = EventoModelSerializer
    filterset_class = EventoFilter
