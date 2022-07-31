from datetime import datetime

from django import views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from litreview.forms.account import RegistrationForm


class Homepage(views.View):
    template_name = '../templates/base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SignUp(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

