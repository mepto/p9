from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.base import TemplateResponseMixin, TemplateView
from rules.contrib.views import PermissionRequiredMixin

from litreview import forms
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


# class ReviewCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class ReviewCreateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """Create a review."""

    model = Review
    permission_required = 'litreview.add_review'
    template_name = 'reviews/review_new.html'
    success_url = reverse_lazy('reviews')
    success_message = "Review created successfully"
    title = 'Create a review'
    # form_class = ReviewForm
    ticket_form_class = TicketForm
    review_form_class = ReviewForm

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = None
        ticket_form = self.ticket_form_class(request.POST, request.FILES, prefix="ticket")
        review_form = self.review_form_class(request.POST, prefix="review")
        print(request.__dict__)
        review_form.user = User.objects.get(id=request.user.id)
        if review_form.is_valid():
            return self.form_valid(review_form)
        else:
            return self.form_invalid(review_form)

    def get(self, request, *args, **kwargs):
        """Get form data."""
        self.object = None
        if 'ticket' in kwargs:
            context = self.get_context_data(ticket=kwargs['ticket'])
        else:
            context = self.get_context_data()
            context['user_id'] = request.user
        return self.render_to_response(context)

    # def form_valid(self, form):
    #     """Check form data."""
    #     form.instance.user = self.request.user
    #     print(form.instance)
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Get context."""
        # context = super().get_context_data()
        context = {}

        request_user = User.objects.get(id=self.request.user.id)
        if 'ticket' in kwargs:
            ticket = Ticket.objects.get(pk=kwargs['ticket'])
            context['ticket_readonly'] = True
            context.update({
                'ticket_data': {
                    'title': ticket,
                    'description': ticket.description,
                    'image': ticket.cover if ticket.image else None,
                    'user': User.objects.get(pk=ticket.user_id),
                }
            })
            context['review_form'] = ReviewForm(initial={'ticket': ticket, 'user': request_user})
        else:
            # self.form_class = {'review_form': ReviewForm, 'ticket_form': TicketForm}
            context['ticket_form'] = TicketForm(prefix='ticket')
            context['review_form'] = ReviewForm(initial={'user': request_user}, prefix='review')
        context['title'] = self.title
        return context


class ReviewEditView(ReviewCreateView, UpdateView):
    """Edit a review."""
    permission_required = 'litreview.change_review'
    title = 'Edit my review request ticket'

    def has_permission(self):
        obj = Review.objects.get(id=self.kwargs['pk'])
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms, obj)

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = Review.objects.get(id=kwargs['review'])
        form = self.get_form()
        if form.is_valid():
            form.instance.id = self.object.id
            form.instance.user = User.objects.get(id=self.object.user_id)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        self.object = None
        if 'review' in kwargs:
            context = self.get_context_data(review=kwargs['review'])
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Call the base implementation first to get the context."""
        context = super().get_context_data(**kwargs)
        self.object = Review.objects.get(id=kwargs['review'])
        ticket_object = Ticket.objects.get(id=self.object.ticket_id)
        review_initial_data = {
            'headline': self.object.headline,
            'rating': self.object.rating,
            'body': self.object.body,
            'user': self.object.user_id,
            'ticket': self.object.ticket_id
        }
        if self.object.user_id == ticket_object.user_id:
            ticket_initial_data = {
                'title': ticket_object.title,
                'description': ticket_object.description,
                'user': ticket_object.user_id,
                'image': ticket_object.image
            }
            context.update({
                'ticket_form': TicketForm(initial=ticket_initial_data),
                'ticket_data': {
                    'image': ticket_object.cover if ticket_object.image else None,
                }})
        else:
            context.update({
                'ticket_data': {
                    'title': ticket_object,
                    'description': ticket_object.description,
                    'user': User.objects.get(pk=ticket_object.user_id),
                    'image': ticket_object.cover if ticket_object.image else None,
                },
                'ticket_readonly': True
            })

        context['review_form'] = ReviewForm(initial=review_initial_data)
        context['title'] = self.title
        return context


class ReviewDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete review created by user."""
    permission_required = 'litreview.delete_review'
    model = Review
    success_url = reverse_lazy('reviews')
    template_name = "confirm_delete.html"
    title = 'Delete review?'

    def has_permission(self):
        obj = Review.objects.get(id=self.kwargs['pk'])
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms, obj)

    def get_context_data(self, **kwargs):
        """Return deletion of confirmation."""
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
