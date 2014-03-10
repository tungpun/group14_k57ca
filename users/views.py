from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from forms import LoginForm, RegisterForm


def auth_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('../../')
                    # Redirect to a success page.
                else:
                    return HttpResponse("Disabled account!")
                    # Return a 'disabled account' error message
            else:
                return HttpResponse("Invalid login.")
                # Return an 'invalid login' error message.
    form = LoginForm()

    return render(request, 'users/auth_login/index.html', {
        'form': form
    })


def auth_logout(request):
    logout(request)
    return HttpResponse("Logout completed!")
    # Redirect to a success page.


def auth_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            if user is not None:
                if user.is_active:
                    #login(request, user)
                    return HttpResponse("Register completed.")
                    # Redirect to a success page.
                else:
                    return HttpResponse("Disabled account!")
                    # Return a 'disabled account' error message
        else:
            return HttpResponse("Invalid Input.")
            # Return an 'invalid login' error message.
    form = RegisterForm()

    return render(request, 'users/auth_register/index.html', {
        'form': form
    })