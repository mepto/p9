from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Ticket(models.Model):
    """Store the tickets."""
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
