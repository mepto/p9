from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from litreview.models.ticket import Ticket

User = get_user_model()


class Review(models.Model):
    """Store the users' reviews."""
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(5)], verbose_name='Book rating')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128, verbose_name='Review headline')
    body = models.TextField(max_length=8192, verbose_name='Review')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.headline
