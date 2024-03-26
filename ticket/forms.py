from django.forms import ModelForm
from servicii.models import ServiciiModel
from ticket.models import TicketModel


class TicketForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obțineți utilizatorul din argumentele trimise la formular
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user  # Inițializați câmpul user cu utilizatorul curent


class SolveTicketForm(ModelForm):
    class Meta:
        model = TicketModel
        fields = "__all__"
