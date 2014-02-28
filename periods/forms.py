__author__ = 'Nguyen Huu Tung'

from django import forms

from timetables.models import Timetable


class EditPeriodForm(forms.Form):
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=30)
    lecturer = forms.CharField(max_length=30)
    position = forms.IntegerField()
    length = forms.IntegerField()
