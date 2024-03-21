from django.forms import ModelForm
from servicii.models import ServiciiModel
from ticket.models import TicketModel


class TicketForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = "__all__"