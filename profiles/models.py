from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model represent a address.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Model function that return user's username.
        """
        return self.user.username
