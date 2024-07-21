from django.contrib import admin
from .models import Support_Ticket

# Register your models here.
@admin.register(Support_Ticket)

class Support_TicketAdmin(admin.ModelAdmin):
    list_display = ('email', 'date', 'issue')
    search_fields = ('email', 'issue')