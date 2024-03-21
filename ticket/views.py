from django.shortcuts import render

# Create your views here.
from ticket.forms import TicketForm
from ticket.models import TicketModel
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView


class CreateTicketView(CreateView):
    model = TicketModel
    form_class = TicketForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('ticket-all')


class UserTicketListView(ListView):
    template_name = 'ticket/user_tickets.html'
    model = TicketModel

    def get_context_data(self, **kwargs):
        data = super(UserTicketListView, self).get_context_data()
        data['tickets'] = TicketModel.objects.filter(user_id=1)
        return data


class TicketDetailsView(DetailView):
    template_name = 'ticket/detalii.html'
    model = TicketModel
from django.shortcuts import render

# Create your views here.
