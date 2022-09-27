from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from rules.contrib.views import PermissionRequiredMixin

from litreview.forms.ticket import TicketForm
from litreview.models import Ticket, User


class TicketCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create new ticket."""
    model = Ticket
    permission_required = 'litreview.add_ticket'
    template_name = 'tickets/ticket_new.html'
    success_url = reverse_lazy('home')
    title = 'Create a ticket for a review request'
    form_class = TicketForm

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = None
        form = self.get_form()
        if form.is_valid():
            form.image = request.FILES
            messages.success(request, f'Ticket "{form.instance.title}" created.')
            return self.form_valid(form)
        else:
            messages.error(request, 'The ticket could not be created. Please check the form and try again.')
            return render(request, self.template_name, {'ticket_form': form})

    def get_context_data(self, **kwargs):
        """Call the base implementation first to get the context."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['ticket_form'] = TicketForm(initial={'user': self.request.user})
        context['request_user'] = self.request.user
        return context


class TicketEditView(TicketCreateView, UpdateView):
    """Edit ticket created by user."""
    permission_required = 'litreview.change_ticket'
    title = 'Edit a review request ticket'

    def has_permission(self):
        obj = Ticket.objects.get(id=self.kwargs['pk'])
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms, obj)

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = Ticket.objects.get(id=self.kwargs['pk'])
        form = self.get_form()
        if form.is_valid():
            form.instance.id = self.object.id
            form.instance.user = User.objects.get(id=self.object.user_id)
            if request.FILES:
                form.instance.image = request.FILES['image']
            else:
                form.instance.image = self.object.image
            messages.success(request, f'The ticket "{form.instance.title}" modified.')
            return self.form_valid(form)
        else:
            messages.error(request, 'Impossible to edit. Please check the form and try again.')
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        """Call the base implementation first to get the context."""
        context = super().get_context_data(**kwargs)
        initial_data = {
            'title': self.object.title,
            'description': self.object.description,
            'image': self.object.image,
            'user': self.object.user
        }
        context['request_user'] = self.object.user
        context['title'] = self.title
        context['ticket_form'] = TicketForm(initial=initial_data)
        return context


class TicketDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete ticket created by user."""
    permission_required = 'litreview.delete_ticket'
    model = Ticket
    success_url = reverse_lazy('home')
    template_name = "confirm_delete.html"
    title = 'Delete ticket?'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Request for review deleted successfully.')
        super().post(request, args, kwargs)

    def has_permission(self):
        obj = Ticket.objects.get(id=self.kwargs['pk'])
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms, obj)

    def get_context_data(self, **kwargs):
        """Return deletion of confirmation."""
        context = super().get_context_data(**kwargs)
        context['item'] = Ticket.objects.get(id=self.kwargs['pk'])
        context['redirect_url'] = self.success_url
        context['title'] = self.title
        return context
