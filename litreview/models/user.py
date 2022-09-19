from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower


class UserManager(BaseUserManager):
    """ Manager for User model """

    def _create_user(self, username, email, password, avatar=None, **extra_fields):
        """Create and save a user."""
        if not email:
            raise ValueError('Users must have an email address bitches')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            user_avatar=avatar.url
        )

        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    """Extend django auth user class."""
    user_avatar = models.ImageField(upload_to="avatars/", blank=True)

    objects = UserManager()

    def __str__(self):
        return self.get_full_name().strip() or self.username

    class Meta:
        app_label = 'litreview'
        swappable = "AUTH_USER_MODEL"
        constraints = [
            models.UniqueConstraint(Lower('email'), name='unique_email')
        ]


class UserFollows(models.Model):
    """Store followed users."""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                      related_name='followed_by')

    class Meta:
        unique_together = ['user', 'followed_user']

    def __str__(self):
        return self.followed_user.username
