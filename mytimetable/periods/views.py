from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from models import Period

def index(request):
    periods_array = Period.objects.all()
    context = {'subjects_array': periods_array}
    return render(request, 'subjects/index.html', context)






#    return HttpResponse("""Subject page""")
