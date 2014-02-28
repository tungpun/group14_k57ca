from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

from models import Period
from forms import EditPeriodForm


def index(request):
    periods_array = Period.objects.all()
    context = {'subjects_array': periods_array}
    return render(request, 'subjects/index.html', context)


def information(request, pid="0"):
    objs = []
    subjects_array = Period.objects.filter(id=pid)
    for subject in subjects_array:
        objs.append(subject)
    content = {
        'period_id': pid,
        'subjects_array': objs
    }
    return render(request, 'subjects/information/index.html', content )


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
    return render(request, 'subjects/edit/index.html', {
        'form': form})