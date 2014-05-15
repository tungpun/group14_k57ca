"""Forms create here"""

from django import forms
from periods.models import Period

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6
DAY_CHOICES = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday')
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
TYPE_PERIOD_CHOICES = (
    (1, 'Science'),
    (2, 'Technology'),
    (3, 'Art'),
    (4, 'Economic'),
    (5, 'Others'),
)


class EditPeriodForm(forms.Form):
    """Form to edit period"""
    code = forms.CharField(max_length=10)
    name = forms.CharField(max_length=30)
    lecturer = forms.CharField(max_length=30)
    day = forms.ChoiceField(
        widget=forms.Select,
        choices=DAY_CHOICES,
    )
    start = forms.ChoiceField(
        widget=forms.Select,
        choices=ORDER_CHOICES,
    )
    length = forms.IntegerField()

    period_type = forms.ChoiceField(
        widget=forms.Select,
        choices=TYPE_PERIOD_CHOICES,
    )

    def check_conflict(self, pid):
        """Check if course conflicts with already-enrolled course"""
        periods_array = Period.objects.filter(timetable_id=pid)
        pos = (int(self.cleaned_data['day']) - 1) * 10
        pos += int(self.cleaned_data['start'])
        leg = self.cleaned_data['length']
        free = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                67, 68, 69, 70, 71, 72, 73]
        for f in free:
            f = False
        for period in periods_array:
            free[period.position] = False
            j = period.position
            while j <= period.position + period.length-1:
                if (j > 0) and (j < 71):
                    free[j] = False
                j += 1
        j = pos
        while j <= pos+leg-1:
            if j > 70:
                return False
            if not free[j]:
                return False
            else:
                free[j] = False
            j += 1
        return True

