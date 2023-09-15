from django.db import models
from django.contrib.auth.models import AbstractUser
import os


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username