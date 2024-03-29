from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from rules.contrib.views import LoginRequiredMixin, PermissionRequiredMixin

from litreview.forms.account import UserFollowForm
from litreview.models import UserFollows


class UserFollowedListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """List all followed users."""
    model = UserFollows
    title = 'Followed users'
    paginate_by = 20
    template_name = 'users/user_follow.html'
    permission_required = 'litreview.view_followers'
    form = UserFollowForm

    def get_context_data(self, **kwargs):
        """Serve full reviews list."""
        self.object_list = super().get_queryset()
        form = self.form
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['following'] = UserFollows.objects.filter(user_id=self.request.user.id)
        context['followed_by'] = UserFollows.objects.filter(followed_user_id=self.request.user.id)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        """Post and save user to follow."""
        self.object = None
        form = self.form(request.POST)
        if form.is_valid():
            follow = form.save(commit=False)
            follow.user_id = request.user.id
            if not UserFollows.objects.filter(Q(followed_user=follow.followed_user) & Q(user_id=follow.user_id)):
                follow.save()
                messages.success(request, f'You are now following {follow.followed_user}')
                return HttpResponseRedirect(reverse_lazy('followed'))
            else:
                context = self.get_context_data()
                context.update({'form': form})
                messages.error(request, 'You are already following this user.')
                return render(request, self.template_name, context)
        else:
            context = self.get_context_data()
            context.update({'form': form})
            messages.error(request, 'This user does not exist.')
            return render(request, self.template_name, context)


class UserUnfollowView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Remove user from followed list."""
    permission_required = 'litreview.delete_followers'
    model = UserFollows
    success_url = reverse_lazy('followed')
    template_name = "confirm_delete.html"
    title = 'Delete follower?'

    def has_permission(self):
        obj = UserFollows.objects.get(id=self.kwargs['pk'])
        perms = self.get_permission_required()
        return self.request.user.has_perms(perms, obj)

    def get_context_data(self, **kwargs):
        """Return deletion of confirmation."""
        context = super().get_context_data(**kwargs)
        context['item'] = UserFollows.objects.get(id=self.kwargs['pk'])
        context['redirect_url'] = self.success_url
        context['title'] = self.title
        return context
