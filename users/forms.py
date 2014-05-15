"""Forms create here"""

from django import forms


class LoginForm(forms.Form):
    """Require username and password to login"""
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128)


class RegisterForm(forms.Form):
    """Require Username, first name, last name, email & password to sign up"""
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=75)
    password = forms.CharField(max_length=128)
