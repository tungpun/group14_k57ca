from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from models import Timetable
from periods.models import Period


def index(request):
    timetables_array = Timetable.objects.all()
    content = {'timetables_array': timetables_array}
    return render(request, 'timetables/index.html', content)


def board(request):
    periods_array = Period.objects.filter(timetable_id=2)
    for period in periods_array:
        period.position -= 1
        period.day = str(period.position / 10)
        period.per = str(period.position % 10)
    content = {'periods_array': periods_array}
    return render(request, 'timetables/board/index.html', content)