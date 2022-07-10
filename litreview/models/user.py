from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Extend django auth user class."""
    user_avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        app_label = 'litreview'
    #     swappable = 'AUTH_USER_MODEL'


class UserFollows(models.Model):
    """Store followed users."""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ['user', 'followed_user']

    def __str__(self):
        return self.followed_user

