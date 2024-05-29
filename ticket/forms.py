from django.forms import ModelForm
from servicii.models import ServiciiModel
from ticket.models import TicketModel
from django import forms
from .models import TicketStatus


class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketModel
        fields = ['nume_societate', 'descriere_ticket', 'status_ticket', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        status_choices = TicketStatus.STATUS_CHOICES
        # Actualizați opțiunile pentru câmpul status_ticket în formular
        self.fields['status_ticket'].widget = forms.Select(choices=status_choices)

        # Verificați dacă există un utilizator asociat cu formularul și, dacă da, inițializați câmpul user
        user = kwargs.get('user')
        if user:
            self.fields['user'].initial = user


class SolveTicketForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = "__all__"


