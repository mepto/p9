from crispy_forms.bootstrap import UneditableField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row
from django.forms import ModelForm, Textarea
from litreview.models import Ticket


class TicketForm(ModelForm):
    """Set form for ticket creation/edition."""

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = Textarea(attrs={'rows': 4, 'cols': 25})
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Field('title', wrapper_class='col-md-9'),
                Column(UneditableField('user', readonly=True,
                css_class='form-control col-md-3', wrapper_class='col-md-3'), css_class="col-md-3 mb-3"),
                Field('user', type="hidden")
            ),
            'description', 'image'
        )
