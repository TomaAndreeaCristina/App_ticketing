from django.contrib import admin

# Register your models here.
from django.contrib import admin

import ticket
from ticket.models import TicketModel

admin.site.register(TicketModel)