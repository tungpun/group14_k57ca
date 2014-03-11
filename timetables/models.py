from django.db import models
from django.contrib.auth.models import User


class Timetable(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    owner = models.IntegerField()