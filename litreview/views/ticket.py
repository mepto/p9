from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from litreview.forms.ticket import TicketForm
from litreview.models import Ticket, User


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


class TicketCreateView(CreateView):
    """Create new ticket."""
    model = Ticket
    template_name = 'tickets/ticket_new.html'
    success_url = reverse_lazy('tickets')
    title = 'Create a ticket for a review request'
    form_class = TicketForm

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        form = self.get_form()
        if form.is_valid():
            form.user = request.user
            form.image = request.FILES
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """Check form data."""
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Call the base implementation first to get the context."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class TicketEditView(TicketCreateView, UpdateView):
    """Edit ticket created by user."""
    title = 'Edit my review request ticket'

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = Ticket.objects.get(id=kwargs['pk'])
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
            'image': self.object.image
        }
        form = TicketForm(initial=initial_data)
        context['title'] = self.title
        context['form'] = form
        return context


class TicketDeleteView(DeleteView):
    """Delete ticket created by user."""
    model = Ticket
    success_url = reverse_lazy('tickets')
    template_name = "confirm_delete.html"
    title = 'Delete ticket?'

    def get_context_data(self, **kwargs):
        """Return deletion of confirmation."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
