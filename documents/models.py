from django.db import models

from ticket.models import TicketModel, TicketStatus


# Create your models here.
class Document(models.Model):
    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='document_storage')

    class Meta:
        app_label = 'documents'