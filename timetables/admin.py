"""Admin management here"""
from django.contrib import admin

# Register your models here.

from models import Timetable

admin.site.register(Timetable)
