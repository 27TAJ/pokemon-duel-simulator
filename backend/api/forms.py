from django import forms
from .models import Support_Ticket

class Support_Ticket_Form(forms.ModelForm):
    class Meta:
        model = Support_Ticket
        fields = ['email', 'date', 'issue']