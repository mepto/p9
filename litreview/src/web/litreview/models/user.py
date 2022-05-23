from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
from django.db import models


User = get_user_model()


class LitUser(User):
    """ Class to extend django auth user class """
    user_avatar = models.ImageField(upload_to="You/media/uploads", blank=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        app_label = 'litreview'


class UserFollows(models.Model):
    """ Class to store followed users """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='followed_by')

    class Meta:
        unique_together = ['user', 'followed_user']

    def __str__(self):
        return self.followed_user

