from django.db import models

# Create your models here.
from timetables.models import Timetable
from django import forms
#class Timetable(models.Model):
 #   pass

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6
DAY_CHOICES = (
    (MONDAY, 'Monday'),
    (TUESDAY, 'Tuesday'),
    (WEDNESDAY, 'Wednesday'),
    (THURSDAY, 'Thursday'),
    (FRIDAY, 'Friday'),
    (SATURDAY, 'Saturday'),
    (SUNDAY, 'Sunday')
)

ORDER_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)

TYPEPERIOD_CHOICES = (
    (1, 'Science'),
    (2, 'Technology'),
    (3, 'Art'),
    (4, 'Economic'),
    (5, 'Others'),
)

class Period(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    lecturer = models.CharField(max_length=30)
    length = models.IntegerField(max_length=2)
    timetable = models.ForeignKey(Timetable)
    position = models.IntegerField(max_length=2)
    period_type = models.CharField(max_length= 30)

