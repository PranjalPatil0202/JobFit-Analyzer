from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any custom fields here
    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username
