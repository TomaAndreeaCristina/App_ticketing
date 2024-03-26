from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from authentication.models import CustomUser


# Create your models here.

class TicketModel(models.Model):
    nume_societate = models.CharField(max_length=50, null=False)
    descriere_ticket = models.TextField(max_length=1000, null=False)
    status_ticket = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    data_inregistrare_ticket = models.DateTimeField(auto_now_add=True, null=False)
    data_inchidere_ticket = models.DateTimeField(auto_now=True, null=False)

    # servicii = models.ForeignKey('ServiciiModel', on_delete=models.DO_NOTHING)
    # def __str__(self):
    #     return f"{self.nume_user} a deschis ticket nr - {self.id}"
