from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from rules.contrib.views import PermissionRequiredMixin

from litreview.forms.review import ReviewForm
from litreview.forms.ticket import TicketForm
from litreview.models import Review, Ticket, User


class ReviewCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create a review."""

    model = Review
    permission_required = 'litreview.add_review'
    template_name = 'reviews/review_new.html'
    success_url = reverse_lazy('home')
    success_message = "Review created successfully"
    title = 'Create a review'
    form_class = None
    ticket_form_class = TicketForm
    ticket_form_prefix = 'ticket'
    review_form_class = ReviewForm
    review_form_prefix = 'review'
    ticket_id = None

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = None
        review_form = self.review_form_class(request.POST, prefix=self.review_form_prefix)
        ticket_form = None
        if 'ticket-user' in request.POST:
            ticket_form = self.ticket_form_class(request.POST, request.FILES, prefix=self.ticket_form_prefix)
            if ticket_form.is_valid():
                ticket = ticket_form.save()
                self.ticket_id = ticket.id
            else:
                return render(request, self.template_name, {'ticket_form': ticket_form, 'review_form': review_form})

        if not self.ticket_id and 'ticket' in kwargs:
            self.ticket_id = int(kwargs['ticket'])

        if Ticket.objects.get(id=self.ticket_id).has_review:
            messages.error(request, 'A review already exists for this request.')
            return HttpResponseRedirect(self.success_url)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket_id = self.ticket_id
            review.save()
            ticket = Ticket.objects.get(id=review.ticket_id)
            ticket.has_review = True
            ticket.save()
            messages.success(request, f'Review "{review.headline}" created successfully.')
            return self.form_valid(review_form)
        else:
            messages.error(request, 'Could not save. Please check the form and try again.')
            return render(request, self.template_name, {'ticket_form': ticket_form, 'review_form': review_form})

    def get(self, request, *args, **kwargs):
        """Get form data."""
        self.object = None
        if 'ticket' in kwargs:
            context = self.get_context_data(ticket=kwargs['ticket'])
        else:
            context = self.get_context_data()
            context['user_id'] = request.user
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """Get context."""
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
            context['review_form'] = ReviewForm(initial={'ticket': ticket, 'user': request_user},
                                                prefix=self.review_form_prefix)
        else:
            context['ticket_form'] = TicketForm(initial={'user': request_user}, prefix=self.ticket_form_prefix)
            context['review_form'] = ReviewForm(initial={'user': request_user}, prefix=self.review_form_prefix)

        context['title'] = self.title

        if self.extra_context is not None:
            context.update(self.extra_context)
        return context


class ReviewEditView(ReviewCreateView, UpdateView):
    """Edit a review."""
    permission_required = 'litreview.change_review'
    title = 'Edit a review'

    def has_permission(self):
        obj = Review.objects.get(id=self.kwargs['review'])
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms, obj)

    def post(self, request, *args, **kwargs):
        """Post and save data."""
        self.object = Review.objects.get(id=kwargs['review'])

        review_form = self.review_form_class(request.POST, prefix=self.review_form_prefix)
        ticket_form = None
        if 'ticket-user' in request.POST:
            ticket_form = self.ticket_form_class(request.POST, request.FILES, prefix=self.ticket_form_prefix)
            ticket_object = Ticket.objects.get(id=self.object.ticket_id)
            if ticket_form.is_valid() and review_form.is_valid():
                ticket = ticket_form.save(commit=False)
                ticket.id = ticket_object.id
                ticket.time_created = ticket_object.time_created
                review = review_form.save(commit=False)
                review.ticket_id = self.object.ticket_id
                review.time_created = self.object.time_created
                review.id = self.object.id
                ticket.save()
                review.save()
                messages.success(request, f'Review "{review.headline}" edited successfully.')
                return self.form_valid(review_form)
            else:
                messages.error(request, 'Could not save. Please check the form and try again.')
                return render(request, self.template_name, {'ticket_form': ticket_form, 'review_form': review_form})
        else:
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.ticket_id = self.object.ticket_id
                review.time_created = self.object.time_created
                review.id = self.object.id
                review.save()
                messages.success(request, f'Review "{review.headline}" edited successfully.')
                return self.form_valid(review_form)
            else:
                messages.error(request, 'Could not save. Please check the form and try again.')
                return render(request, self.template_name, {'ticket_form': ticket_form, 'review_form': review_form})

    def get(self, request, *args, **kwargs):
        self.object = None
        context = None
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
                'ticket_form': TicketForm(initial=ticket_initial_data, prefix='ticket'),
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

        context['review_form'] = ReviewForm(initial=review_initial_data, prefix='review')
        context['title'] = self.title
        return context


class ReviewDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete review created by user."""
    permission_required = 'litreview.delete_review'
    model = Review
    success_url = reverse_lazy('home')
    template_name = "confirm_delete.html"
    title = 'Delete review?'

    def post(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(id=Review.objects.get(id=self.kwargs['pk']).ticket_id)
        ticket.has_review = False
        ticket.save()
        messages.success(request, 'Review deleted successfully.')
        return super().post(request, args, kwargs)

    def has_permission(self):
        obj = Review.objects.get(id=self.kwargs['pk'])
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms, obj)

    def get_context_data(self, **kwargs):
        """Return deletion of confirmation."""
        context = super().get_context_data(**kwargs)
        context['item'] = Review.objects.get(id=self.kwargs['pk'])
        context['redirect_url'] = self.success_url
        context['title'] = self.title
        return context
