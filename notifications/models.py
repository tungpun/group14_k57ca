"""Models initialize here"""
from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
    """Notification properties"""
    text = models.CharField(max_length=512)
    userID = models.ForeignKey(User)
    new = models.BooleanField()
