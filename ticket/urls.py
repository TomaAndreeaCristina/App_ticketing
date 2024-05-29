from django.urls import path,  include
from servicii.views import ServiciiUpdateView, ServiciiCreateView, ServiciiDeleteView
from ticket.views import TicketDetailsView, UserTicketListView, CreateTicketView, CreateUpdateFormView, EditTicketView, \
    DeleteTicketView, ListaTicketView, EditTicketIdView
from . import views

urlpatterns = [
    path('', UserTicketListView.as_view(), name='ticket-all'),
    path('create/', CreateTicketView.as_view(), name='ticket-add'),
    path('user_tickets/', UserTicketListView.as_view(), name='user_tickets'),
    path('create_update/', CreateUpdateFormView.as_view(), name='create_update'),
    path('detail/<int:pk>', TicketDetailsView.as_view(), name='ticket-detail'),
    path('edit-ticket/<int:ticket_id>/', EditTicketView.as_view(), name='edit-ticket'),
    path('delete-ticket/<int:ticket_id>/', DeleteTicketView.as_view(), name='delete_ticket'),
    # path('lista_tickete/', ListaTicketView.as_view(), name='lista_tickete'),
    path('lista_tickete/', views.index, name='index'),
    path('ticket/<int:ticket_id>/', views.ticket_by_id, name='ticket-detail'),
    path('edit-idticket/<int:ticket_id>/', EditTicketIdView.as_view(), name='edit-idticket'),
]
