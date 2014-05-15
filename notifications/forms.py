"""Forms create here"""
from django.contrib.auth.models import User
from django import forms


class GetNotification(forms.Form):
    """Notification form"""
    text = forms.CharField(max_length=512)
    userID = forms.IntegerField(User)
    new = forms.BooleanField()

