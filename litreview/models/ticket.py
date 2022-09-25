from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Ticket(models.Model):
    """Store the tickets."""
    title = models.CharField(max_length=128, verbose_name='Request title')
    description = models.TextField(max_length=2048, blank=True, verbose_name='Request description')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='covers/', null=True, blank=True, verbose_name='Book image')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.title

    @property
    def cover(self):
        """Provide url to covers."""
        return self.image.url
