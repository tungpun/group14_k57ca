from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from forms import LoginForm, RegisterForm


def auth_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("../../")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('../../users/gateway/do=2')
                    # Redirect to a success page.
                else:
                    return HttpResponse("Disabled account!")
                    # Return a 'disabled account' error message
            else:
                return HttpResponseRedirect('../../users/gateway/do=4')
                # Return an 'invalid login' error message.
    form = LoginForm()

    return render(request, 'users/auth_login/index.html', {
        'form': form
    })


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("../../users/gateway/do=3")
    # Redirect to a success page.


def auth_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("../../")
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
                    return HttpResponseRedirect("../../users/gateway/do=1")
                    # Redirect to a success page.
                else:
                    return HttpResponse("Disabled account!")
                    # Return a 'disabled account' error message
        else:
            return HttpResponseRedirect("../../users/gateway/do=4")
            # Return an 'invalid login' error message.
    form = RegisterForm()

    return render(request, 'users/auth_register/index.html', {
        'form': form
    })


def gateway(request, pid="0"):
    message = "Hacker detected!"
    if pid == "1":      # Register
        message = "Register completed. Have fun with Time Machine :)"
    elif pid == "2":     # Login
        message = "Login completed! Have fun with Time Machine :)"
    elif pid == "3":      # Logout
        message = "Have good journey. See you again ;)"
    elif pid == "4":
        message = "Invalid login."
    elif pid == "5":
        message = "GET Period failed. Please choose another one!!!"
    elif pid == "6":
        message = "Wrong input. Try again!!!"
    elif pid == "7":
        message = "You have no right to edit this period!"
    return render(
        request,
        'users/gateway/index.html', {
            'message': message,
            'pid': pid
        }
    )