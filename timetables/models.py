"""Models initialize here"""
from django.db import models


class Timetable(models.Model):
    """Timetable properties"""
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    owner = models.IntegerField()
