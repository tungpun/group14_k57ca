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
    objs = []

    periods_array = Period.objects.filter(timetable_id=2)
    for period in periods_array:
        objs.append(period)

    for i in range(0, 71):
        free = True
        for period in periods_array:
            if period.position == i:
                free = False
                break
        if free:
            mark = False
            for period in periods_array:
                if (period.position < i) and (i < period.position + period.length):
                    mark = True
                    break
            if mark:
                objs.append(Period(position=i, name=0))
            else:
                objs.append(Period(position=i, name=""))

    for obj in objs:
        obj.day = str((obj.position - 1) / 10)
        obj.per = str((obj.position - 1) % 10)

    objs.sort(key=lambda obj: obj.position)
    #objs.sort(cmp=None,key=position,request=False)

    content = {'periods_array': objs}
    return render(request, 'timetables/board/index.html', content)