# Create your views here.
from rest_framework import viewsets

from ticket.forms import TicketForm, SolveTicketForm
from ticket.models import TicketModel
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView, TemplateView
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.views.generic import View
from django.shortcuts import render
from user.models import UserModel
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CreateTicketView(CreateView):
    model = TicketModel
    form_class = TicketForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('ticket-all')

    def form_valid(self, form):
        ticket = form.save(commit=False)  # Se salveaza formularul, dar nu nu se comite încă
        ticket.user = self.request.user  # Asociaza utilizatorul curent cu ticketul
        ticket.save()  # Salveaza ticketul împreună cu utilizatorul asociat

        # Redirecționare către pagina utilizatorului asociat cu ticketul
        return redirect('user_tickets')
        # user_id=self.request.user.id)  # 'user_tickets'


class UserTicketListView(ListView):
    template_name = 'ticket/user_tickets.html'
    model = TicketModel
    context_object_name = 'tickets'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tickets'] = TicketModel.objects.filter(user=self.request.user)
        return data


class UserTicketListIdView(ListView):
    template_name = 'ticket/ticket_by_id.html'
    model = TicketModel
    context_object_name = 'tickets'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tickets'] = TicketModel.objects.filter(user=self.request.user)
        return data


class TicketDetailsView(DetailView):
    template_name = 'ticket/detalii.html'
    model = TicketModel


class SolveTicketView(UpdateView):
    model = TicketModel
    form_class = SolveTicketForm
    template_name = 'ticket/solve_ticket_form.html'
    success_url = reverse_lazy('user_tickets')

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.data_inchidere_ticket = timezone.now()  # Actualizare data de închidere a tichetului la momentul modificarilor
        ticket.save()
        return super().form_valid(form)


class CreateUpdateFormView(TemplateView):
    template_name = 'ticket/user_tickets.html'


class EditTicketView(View):
    def post(self, request, ticket_id):
        modificari = request.POST.get('modificari')
        ticket = TicketModel.objects.get(pk=ticket_id)

        # Actualizăm descrierea tichetului cu modificările introduse
        ticket.descriere_ticket += f"\n Modificări: {modificari} {ticket.data_inchidere_ticket}\n"
        ticket.save()

        return redirect('user_tickets')


class EditTicketIdView(View):
    def get(self, request, ticket_id):
        # Add code to handle GET requests here
        ticket = TicketModel.objects.get(pk=ticket_id)
        return render(request, 'ticket/ticket_by_id.html', {'ticket': ticket})

    def post(self, request, ticket_id):
        # Add code to handle POST requests here
        modificari = request.POST.get('modificari')
        ticket = TicketModel.objects.get(pk=ticket_id)

        # Actualizăm descrierea tichetului cu modificările introduse
        ticket.descriere_ticket += f"\n Modificări: {modificari} {ticket.data_inchidere_ticket}\n"
        ticket.save()

        # Redirect back to the same view with the same ticket_id
        return redirect(reverse('edit-idticket', kwargs={'ticket_id': ticket_id}))


class DeleteTicketView(DeleteView):
    template_name = 'ticket/delete_ticket.html'
    success_message = "Ticket Sters cu succes"
    model = TicketModel
    success_url = reverse_lazy('user_tickets')

    def get_object(self, queryset=None):
        ticket_id = self.kwargs.get('ticket_id')
        return TicketModel.objects.get(pk=ticket_id)


class ListaTicketView(ListView):
    template_name = 'ticket/lista_tickete.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return UserModel.objects.prefetch_related('tickets').all()


def index(request):
    tickets = TicketModel.objects.order_by('data_inregistrare_ticket')[:50]
    return render(request, 'ticket/index.html', {'tickets': tickets})


def ticket_by_id(request, ticket_id):
    ticket = TicketModel.objects.get(pk=ticket_id)
    return render(request, 'ticket/ticket_by_id.html', {'ticket': ticket})


