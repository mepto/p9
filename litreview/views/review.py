from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rules.contrib.views import PermissionRequiredMixin

from litreview.forms.review import ReviewForm
from litreview.forms.ticket import TicketForm
from litreview.models import Review, Ticket, User


class ReviewListView(ListView):
    """List all reviews."""
    model = Review
    queryset = Review.objects.all()
    template_name = 'reviews/review_list.html'
    title = 'Existing reviews list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Serve full reviews list."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['data'] = Review.objects.all()
        return context

