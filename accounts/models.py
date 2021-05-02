from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bot = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.URLField(blank=True, null=True)
    school = models.CharField(max_length=200)