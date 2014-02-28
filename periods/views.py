from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

from models import Period

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
        'period_id' : pid,
        'subjects_array' : objs
    }
    return render(request, 'subjects/information/index.html', content )








#    return HttpResponse("""Subject page""")
