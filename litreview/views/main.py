from itertools import chain

from django.db.models import CharField, Q, Value
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from rules.contrib.views import LoginRequiredMixin, PermissionRequiredMixin

from litreview.forms.account import RegistrationForm
from litreview.models import Review, Ticket, User, UserFollows


class HomepageFeed(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Display feed for user on homepage with posts from users followed and own posts."""
    template_name = 'homepagefeed.html'
    # paginate_by = 10
    permission_required = 'litreview.view_homepagefeed'
    queryset = None
    title = 'My tickets and reviews feed'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Retrieve context data."""
        qs = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['data'] = qs
        context['request_user'] = self.request.user
        return context

    def get_queryset(self, own_only=False):
        """Return full queryset available to user."""
        current_user = self.request.user
        _filter = Q(user=current_user)
        if not own_only:
            _filter = _filter | Q(user__in=current_user.followers)

        tickets = Ticket.objects.filter(_filter).annotate(
            post_type=Value('ticket', CharField()))

        reviews = Review.objects.filter(_filter | Q(ticket__user=current_user)).annotate(
            post_type=Value('review', CharField())).select_related('ticket')
        return sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)


class OwnFeed(HomepageFeed):
    """Display own posts."""
    title = 'My own requests and reviews'
    permission_required = 'litreview.view_ownfeed'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset(own_only=True)


class SignUp(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfile(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'users/user_profile.html'
    title = 'User profile'
    permission_required = 'litreview.view_profile'

    def get(self, request, *args, **kwargs):
        user = request.user
        context = self.get_context_data(**kwargs)
        context['title'] = self.title
        return self.render_to_response(context)
