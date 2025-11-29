# tickets/views.py

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from django.db.models import Q
from .models import Ticket, Customer, Alert
from .serializers import TicketSerializer, CustomerSerializer, AlertSerializer
from .tasks import classify_ticket_task, compute_churn_for_customer  # <--- importar tarea Celery

# ----------------------------
# DRF API ViewSets
# ----------------------------
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TicketViewSet(viewsets.ModelViewSet):
    """ViewSet para tickets con soporte de búsqueda y paginación.

    Parámetros aceptados (query params):
    - search: texto para buscar en título y descripción
    - customer_id: filtrar por cliente
    - page: número de página (DRF PageNumberPagination)
    """
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = Ticket.objects.all().order_by('-created_at')
        params = self.request.query_params
        search = params.get('search')
        customer_id = params.get('customer_id')
        if customer_id:
            try:
                qs = qs.filter(customer__id=int(customer_id))
            except (ValueError, TypeError):
                pass
        if search:
            qs = qs.filter(Q(title__icontains=search) | Q(description__icontains=search))
        return qs

    def perform_create(self, serializer):
        """
        Al crear un ticket, lanzamos:
        1️⃣ Clasificación automática
        2️⃣ Cálculo de churn del cliente
        """
        ticket = serializer.save()
        classify_ticket_task.delay(ticket.id)                   # Clasificación IA
        compute_churn_for_customer.delay(ticket.customer.id)    # Calcular churn automáticamente

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

# ----------------------------
# Dashboard Views (HTML)
# ----------------------------
def dashboard_view(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    alerts = Alert.objects.filter(handled=False).order_by('-created_at')
    customers = Customer.objects.all()

    # Calcular métricas generales
    total_tickets = tickets.count()
    total_alerts = alerts.count()
    high_risk_customers = customers.filter(churn_risk__gte=0.7).count()

    context = {
        'tickets': tickets,
        'alerts': alerts,
        'customers': customers,
        'total_tickets': total_tickets,
        'total_alerts': total_alerts,
        'high_risk_customers': high_risk_customers,
    }

    return render(request, 'dashboard.html', context)
