from django.contrib import admin

# Register your models here.
from django.contrib import admin

import ticket
from .models import TicketModel


class TicketAdmin(admin.ModelAdmin):
    list_display = ('nume_societate', 'descriere_ticket', 'status_ticket', 'user', 'data_inregistrare_ticket', 'data_inchidere_ticket')
    list_filter = ('status_ticket', 'user')
    date_hierarchy = 'data_inregistrare_ticket'


admin.site.register(TicketModel, TicketAdmin)


