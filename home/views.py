from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from ticket.models import TicketModel


# Create your views here.


def home(request):
    return render(request, template_name='home/home.html')


class HomeView(ListView):
    template_name = 'home/home.html'
    model = TicketModel

