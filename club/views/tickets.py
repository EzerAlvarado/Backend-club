from django.shortcuts import render

# Create your views here.
#models
from club.models import Ticket
#rest
from rest_framework import viewsets
#utilities
from club.serializers.tickets import TicketModelSerializer
#filters
from club.filters.tickets import TicketFilter

class TicketViewSet(viewsets.ModelViewSet):
    """
    View de Tickets
    Maneja CRUD
    """
    queryset=Ticket.objects.all()
    serializer_class = TicketModelSerializer
    filterset_class = TicketFilter
