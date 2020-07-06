from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100, blank=True)
