from django.db import models

# Create your models here.

class Timetable(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)