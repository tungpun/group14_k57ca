from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

from models import Period
from forms import EditPeriodForm


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')

    periods_array = Period.objects.all()
    context = {'periods_array': periods_array}
    return render(request, 'periods/index.html', context)


def detail(request, pid="0"):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')

    objs = []
    periods = Period.objects.filter(id=pid)
    if not periods.exists():
        return HttpResponse("Period not found!")

    for period in periods:
        objs.append(period)
    content = {
        'period_id': pid,
        'periods': objs,
    }
    return render(request, 'periods/detail/index.html', content)

def check_conflict2(periods, pid):
        periods_array = Period.objects.filter(id=pid)
        pos = periods.position
        leg = periods.length
        free = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]
        for f in free:
            f = True
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

def get(request, pid='0'):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')
    if request.method == 'GET':
                current_user = request.user
                periods = Period.objects.get(id=pid)
                new_period = Period(code=periods.code,
                                    name=periods.name,
                                    lecturer=periods.lecturer,
                                    position=periods.position,
                                    length=periods.length,
                                    timetable_id=current_user.id)
                if check_conflict2(periods, current_user.id):
                    new_period.save()
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Can't get this subject")
					
def edit(request, pid="0"):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')

    if request.method == 'POST':            # if the form has been submitted...
        form = EditPeriodForm(request.POST)             # A form bound to the POST data
        if form.is_valid() and form.check_conflict(pid):          # All validation rules pass
            Period.objects.filter(id=pid).update(code=form.cleaned_data['code'],
                                                 name=form.cleaned_data['name'],
                                                 lecturer=form.cleaned_data['lecturer'],
                                                 position=(int(form.cleaned_data['day']) - 1) * 10 + int(form.cleaned_data['start']),
                                                 length=form.cleaned_data['length'])
            return HttpResponseRedirect('/periods/id='+pid)           # Redirect after POST
        else:
            return HttpResponse("Wrong Input! Try again, pls")
    else:
        form = EditPeriodForm()
    return render(request, 'periods/edit/index.html', {
        'form': form})


def add(request, pid="0"):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')

    if request.method == 'POST':            # if the form has been submitted...
        form = EditPeriodForm(request.POST)             # A form bound to the POST data
        if form.is_valid() and form.check_conflict(pid):          # All validation rules pass
            new_period = Period(
                code=form.cleaned_data['code'],
                name=form.cleaned_data['name'],
                lecturer=form.cleaned_data['lecturer'],
                position=(int(form.cleaned_data['day']) - 1) * 10 + int(form.cleaned_data['start']),
                length=form.cleaned_data['length'],
                timetable_id=pid)
            new_period.save()
            return HttpResponseRedirect('/')           # Redirect after POST
        else:
            return HttpResponse("Wrong Input! Try again, pls")
    else:
        form = EditPeriodForm()

    return render(
        request,
        'periods/edit/index.html', {
            'form': form
        }
    )