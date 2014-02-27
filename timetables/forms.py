__author__ = 'Nguyen Huu Tung'

from django import forms


class InsertTimetableForm(forms.Form):
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=30)