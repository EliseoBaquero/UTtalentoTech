from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

PRIORITY_CHOICES = [('low','Low'), ('medium','Medium'), ('high','High')]

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    churn_risk = models.FloatField(default=0.0)  # probabilidad de churn

    def __str__(self):
        return f"{self.name} ({self.company})"

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    created_at = models.DateTimeField(auto_now_add=True)
    classified = models.BooleanField(default=False)  # si ya pasó por ML
    is_security = models.BooleanField(default=False)  # marcada como amenaza
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.title[:30]}"

class Alert(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='alerts')
    message = models.CharField(max_length=400)
    level = models.CharField(max_length=50)  # e.g. critical, warning
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

class ModelRecord(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    path = models.CharField(max_length=400)  # ruta en disco o S3
    trained_at = models.DateTimeField(auto_now_add=True)

# ───────────────
# Receiver para enviar tickets a Celery
# ───────────────
@receiver(post_save, sender=Ticket)
def process_ticket(sender, instance, created, **kwargs):
    """
    Enviar automáticamente ticket nuevo a Celery
    """
    if created:
        # Importar aquí dentro para evitar circular import
        from .tasks import classify_ticket_task
        classify_ticket_task.delay(instance.id)
