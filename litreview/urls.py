"""litreview URL Configuration."""
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from litreview.views.follow import UserFollowedListView, UserUnfollowView
from litreview.views.main import Homepage, SignUp, UserProfile
from litreview.views.review import ReviewCreateView, ReviewDeleteView, ReviewEditView, ReviewListView
from litreview.views.ticket import TicketCreateView, TicketDeleteView, TicketEditView, TicketListView

urlpatterns = [
    path('home/', Homepage.as_view(), name='home'),
    path('', Homepage.as_view(), name='home'),
    path("signup/", SignUp.as_view(), name="signup"),
    path("profile/", UserProfile.as_view(), name="profile"),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket-new'),
    path('ticket/edit/<int:pk>/', TicketEditView.as_view(), name='ticket-edit'),
    path('ticket/delete/<int:pk>/', TicketDeleteView.as_view(), name='ticket-delete'),
    path('ticket/list/', TicketListView.as_view(), name='tickets'),
    path('review/new/<int:ticket>/', ReviewCreateView.as_view(), name='review-new'),
    path('review/new/', ReviewCreateView.as_view(), name='review-new'),
    path('review/edit/<int:review>/', ReviewEditView.as_view(), name='review-edit'),
    path('review/delete/<int:pk>/', ReviewDeleteView.as_view(), name='review-delete'),
    path('review/list/', ReviewListView.as_view(), name='reviews'),
    path('following/list/', UserFollowedListView.as_view(), name='followed'),
    path('following/unfollow/<int:pk>', UserUnfollowView.as_view(), name='unfollow'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
