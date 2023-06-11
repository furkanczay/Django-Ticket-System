from django.forms import ModelForm, Select
from .models import Ticket


class AddTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['status', 'agent', 'completed_at', 'user']
        widgets = {
            'priority': Select(attrs={'class': 'form-select'}),
            'category': Select(attrs={'class': 'form-select'})
        }
