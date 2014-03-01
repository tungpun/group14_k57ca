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