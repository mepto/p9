from django.forms import ModelForm
from litreview.models import Ticket


class TicketForm(ModelForm):
    """Set form for ticket creation/edition."""

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
