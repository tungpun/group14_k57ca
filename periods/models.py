from django.db import models

# Create your models here.
from timetables.models import Timetable

#class Timetable(models.Model):
 #   pass


class Period(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    lecturer = models.CharField(max_length=30)
    position = models.IntegerField(max_length=2)
    length = models.IntegerField(max_length=2)
    timetable = models.ForeignKey(Timetable)