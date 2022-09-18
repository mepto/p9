from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Row, Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

from litreview.models import User, UserFollows


class RegistrationForm(UserCreationForm):
    """Create form for user registration."""
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'user_avatar')


class UserFollowForm(forms.ModelForm):
    """Create form for following users."""
    followed_user = forms.CharField(max_length=150)

    class Meta:
        model = UserFollows
        fields = ('followed_user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['followed_user'].label = ''

    def clean_followed_user(self):
        data = self.cleaned_data['followed_user']
        try:
            user = User.objects.filter(username=data).first()
        except User.DoesNotExist:
            raise ValidationError('No such username')
        return user
