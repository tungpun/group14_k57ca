from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

from models import Period
from forms import EditPeriodForm


def index(request):
    periods_array = Period.objects.all()
    context = {'periods_array': periods_array}
    return render(request, 'periods/index.html', context)


def detail(request, pid="0"):
    objs = []
    periods = Period.objects.filter(id=pid)
    for period in periods:
        objs.append(period)
    content = {
        'period_id': pid,
        'periods': objs,
    }
    return render(request, 'periods/detail/index.html', content)


def edit(request, pid="0"):
    if request.method == 'POST':            # if the form has been submitted...
        form = EditPeriodForm(request.POST)             # A form bound to the POST data
        if form.is_valid():          # All validation rules pass
            Period.objects.filter(id=pid).update(code=form.cleaned_data['code'],
                                                 name=form.cleaned_data['name'],
                                                 lecturer=form.cleaned_data['lecturer'],
                                                 position=form.cleaned_data['position'],
                                                 length=form.cleaned_data['length'])
            return HttpResponseRedirect('/periods/id='+pid)           # Redirect after POST
    else:
        form = EditPeriodForm()
    return render(request, 'periods/edit/index.html', {
        'form': form})

def add(request, pid="0"):

    if request.method == 'POST':            # if the form has been submitted...
        form = EditPeriodForm(request.POST)             # A form bound to the POST data
        if form.is_valid():          # All validation rules pass
            periods_array=Period.objects.filter(timetable_id=pid)
            pos = form.cleaned_data['position']
            leg = form.cleaned_data['length']
            free = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                    57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,71, 72, 73]
            for i in free:
                i = True
            for period in periods_array:
                free[period.position] = False
                j = period.position
                while j <= period.position+period.length-1:
                    if j > 0 and j < 71:
                        free[j] = False
                    j += 1


            j = pos
            while j <= pos+leg-1:
                if j > 70:
                    return HttpResponse("Out of Range!!!")
                if free[j] == False:
                    return HttpResponse("Input Error!!!")
                else:
                    free[j] = False
                    j += 1

            new_period = Period(code=form.cleaned_data['code'], name=form.cleaned_data['name'],
                lecturer=form.cleaned_data['lecturer'], position=form.cleaned_data['position'],
                length=form.cleaned_data['length'], timetable_id=pid)
            new_period.save()
            return HttpResponseRedirect('/timetables/id='+pid)           # Redirect after POST
    else:
        form = EditPeriodForm()
    return render(request, 'periods/edit/index.html', {
        'form': form})