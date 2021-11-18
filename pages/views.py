from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import CreateUserForm
from django.contrib import messages


# Create your views here.


def login_view(request, *args, **kwargs):
    context = {}
    return render(request, "login.html", context)


def signup_view(request, *args, **kwargs):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account Has Been Created! ')

    context = {'form': form}
    return render(request, "signup.html", context)


def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "home.html", context)
