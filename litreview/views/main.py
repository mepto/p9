from datetime import datetime

from django import views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from litreview.forms.account import RegistrationForm


class Homepage(views.View):
    template_name = '../templates/base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SignUp(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfile(TemplateView):
    template_name = '../templates/users/user_profile.html'
    title = 'User profile'

    def get(self, request, *args, **kwargs):
        user = request.user
        context = self.get_context_data(**kwargs)
        context['title'] = self.title
        return self.render_to_response(context)
