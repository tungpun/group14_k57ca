__author__ = 'Nguyen Huu Tung'

from django import forms

from timetables.models import Timetable

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

class EditPeriodForm(forms.Form):
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=30)
    lecturer = forms.CharField(max_length=30)
    position = forms.IntegerField()
    length = forms.IntegerField()
    day = forms.ChoiceField(widget=forms.Select,
                                         choices=DAY_CHOICES,)
    start = forms.ChoiceField(widget=forms.Select,
                                choices=ORDER_CHOICES,)
