from datetime import datetime

from django import views
from django.shortcuts import render


class Homepage(views.View):
    template_name = '../templates/base.html'

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        return render(request, self.template_name, {'date': now})