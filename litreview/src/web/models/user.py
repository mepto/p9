from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_avatar = models.ImageField(upload_to="You/media/uploads", blank=True)


class UserFollows(models.Model):
    pass

