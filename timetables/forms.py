"""Forms create here"""
from django import forms


class InsertTimetableForm(forms.Form):
    """Form to create Timetable"""
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=30)
