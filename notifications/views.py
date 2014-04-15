from django.shortcuts import render
from django.contrib.auth.models import User
from forms import GetNotification
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import Notification
# Create your views here.

def sendNotification (request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/users/auth_login')

    if request.method == 'POST':
        form = GetNotification(request.POST)
        if form.is_valid():
            new_noti = Notification(text = form.cleaned_data['text'],
                                    userID = form.cleaned_data['userID'],
                                    new = True)
            new_noti.save()
            return HttpResponseRedirect('/')           # Redirect after POST
        else:
            return HttpResponseRedirect('/users/gateway/do=6')
    else:
        form = GetNotification()

    return render(request, 'notifications/send/index.html', {
        'form': form})

