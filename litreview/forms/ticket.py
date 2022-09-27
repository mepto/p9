from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Row
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
        user_layout = Layout(Field('user', readonly=True, type="hidden"))
        if 'disabled' in kwargs and kwargs['disabled']:
            self.helper.layout = Layout(
                user_layout,
                Row(
                    Field('title', readonly=True, wrapper_class='col-md-9'),
                    Field('user', readonly=True, type="hidden"),
                ),
                Field('description', readonly=True), Field('image', readonly=True)
            )
        else:
            self.helper.layout = Layout(
                user_layout,
                Row(
                    Field('title', wrapper_class='col-md-9'),
                ),
                Field('description'), Field('image')
            )
