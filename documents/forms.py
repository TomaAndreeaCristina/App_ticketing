from django.forms import ModelForm
from servicii.models import ServiciiModel
from ticket.models import TicketModel
from django import forms
from .models import TicketStatus


class ProfileimageForm(forms.Form):
    document = forms.FileField(label="Atasati un document")