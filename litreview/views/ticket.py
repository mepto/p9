from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rules.contrib.views import PermissionRequiredMixin

from litreview.forms.ticket import TicketForm
from litreview.models import Ticket, User


# TODO: make tz aware


class TicketListView(ListView):
    """List review request tickets."""
    model = Ticket
    queryset = Ticket.objects.all()
    template_name = 'tickets/ticket_list.html'
    title = 'Existing tickets list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Serve full ticket list."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['data'] = Ticket.objects.all()
        return context


class TicketCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create new ticket."""
    model = Ticket
    permission_required = 'litreview.add_ticket'
    template_name = 'tickets/ticket_new.html'
    success_url = reverse_lazy('tickets')
    title = 'Create a ticket for a review request'
    form_class = TicketForm

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = None
        form = self.get_form()
        if form.is_valid():
            form.image = request.FILES
            return self.form_valid(form)
        else:
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
    title = 'Edit my review request ticket'

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
            return self.form_valid(form)
        else:
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
    success_url = reverse_lazy('tickets')
    template_name = "confirm_delete.html"
    title = 'Delete ticket?'

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
