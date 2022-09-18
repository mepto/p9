from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Row
from django.forms import CharField, ModelForm, Textarea, forms
from litreview.models import Review


class ReviewForm(ModelForm):
    """Set form for ticket creation/edition."""

    class Meta:
        model = Review
        fields = ['rating', 'user', 'headline', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['user'].label = False
        self.fields['headline'].label = 'Your headline review'
        self.fields['body'].label = 'Your review'
        self.fields['rating'].label = 'Your rating'
        self.fields['body'].widget = Textarea(attrs={'rows': 4, 'cols': 25})
        self.helper.layout = Layout(
            Field('user', hidden=True, readonly=True),
            Row(Field('headline', wrapper_class='col-md-9'),
                Field('rating', wrapper_class='col-md-3')),
            'body'
        )
