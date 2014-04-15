__author__ = 'HoangVuong'
from django.contrib.auth.models import User
from django import forms

class GetNotification(forms.Form):
    text = forms.CharField(max_length=512)
    userID = forms.IntegerField(User)
    new = forms.BooleanField()

