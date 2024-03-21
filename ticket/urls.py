from django.urls import path
from servicii.views import ServiciiUpdateView, ServiciiCreateView, ServiciiDeleteView
from ticket.views import TicketDetailsView, UserTicketListView, CreateTicketView


urlpatterns = [
    path('', UserTicketListView.as_view(), name='ticket-all'),
    path('create/', CreateTicketView.as_view(), name='ticket-add'),
    path('detail/<int:pk>', TicketDetailsView.as_view(), name='ticket-detail'),
]