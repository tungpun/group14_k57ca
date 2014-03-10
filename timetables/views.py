from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

from models import Timetable
from periods.models import Period
from forms import InsertTimetableForm


def index(request):
    return render(request, 'timetables/index.html')


def board(request, pid="0"):    # default of pid is 1
    objs = []

    periods_array = Period.objects.filter(timetable_id=pid)
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
                objs.append(Period(position=i, name="", length=0))

    for obj in objs:
        obj.day = str((obj.position - 1) / 10)
        obj.per = str((obj.position - 1) % 10)

    objs.sort(key=lambda obj: obj.position)
    #objs.sort(cmp=None,key=position,request=False)

    current_user = request.user
    if not current_user.is_authenticated():
        request.user = 'Guest'
        #return render(request, '/../users/login')
        return HttpResponseRedirect('/users/auth_login')
    else:
        content = {
            'timetable_id': pid,
            'periods_array': objs,
            'username': current_user
        }
        return render(request, 'timetables/board/index.html', content)


def add(request):             # add Timetable
    if request.method == 'POST':            # if the form has been submitted...
        form = InsertTimetableForm(request.POST)             # A form bound to the POST data
        if form.is_valid():          # All validation rules pass
            new_timetable = Timetable(code=form.cleaned_data['code'], name=form.cleaned_data['name'])
            new_timetable.save()
            return HttpResponseRedirect('/timetables/')           # Redirect after POST
    else:
        form = InsertTimetableForm()

    return render(request, 'timetables/add/index.html', {
        'form': form})