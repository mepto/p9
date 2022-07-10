"""litreview URL Configuration."""
from django.contrib import admin
from django.urls import path

from litreview.views.main import Homepage

urlpatterns = {

    path('admin/', admin.site.urls),
    path('home/', Homepage.as_view(), name='home'),
    path('', Homepage.as_view(), name='home'),
}