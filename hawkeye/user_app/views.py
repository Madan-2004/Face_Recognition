from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserRegistrationForm, UserLoginForm
from hawkeye import views

def login_or_register(request):
    login_form = UserLoginForm()
    registration_form = UserRegistrationForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            registration_form = UserRegistrationForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                return redirect(views.home)

        else:
            login_form = UserLoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(views.home)
    return render(request, 'login_or_register.html', {'login_form': login_form, 'registration_form': registration_form})

def user_logout(request):
    logout(request)
    return redirect(views.home) 