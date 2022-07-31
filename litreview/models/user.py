from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Extend django auth user class."""
    user_avatar = models.ImageField(upload_to="avatars/", blank=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        app_label = 'litreview'
        swappable = "AUTH_USER_MODEL"

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        # user.save(using=self._db)
        return user


class UserFollows(models.Model):
    """Store followed users."""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ['user', 'followed_user']

    def __str__(self):
        return self.followed_user
