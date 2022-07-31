"""litreview URL Configuration."""
from django.urls import include, path

from litreview.views.main import Homepage, SignUp

urlpatterns = [
    path('home/', Homepage.as_view(), name='home'),
    path('', Homepage.as_view(), name='home'),
    path("signup/", SignUp.as_view(), name="signup"),
]

