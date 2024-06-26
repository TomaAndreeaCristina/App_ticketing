from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from authentication.models import CustomUser
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TicketStatus(models.Model):
    STATUS_CHOICES = (
        ("Nou", 'Nou'),
        ("Preluat", 'Preluat'),
        ("Inchis", 'Inchis'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Nou")


class TicketModel(models.Model):
    nume_societate = models.CharField(max_length=50, null=False)
    descriere_ticket = models.TextField(max_length=1000, null=False)
    status_ticket = models.CharField(max_length=20, choices=TicketStatus.STATUS_CHOICES, default='Nou')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    data_inregistrare_ticket = models.DateField(auto_now_add=True, null=False)
    data_inchidere_ticket = models.DateField(auto_now=True, null=False)








