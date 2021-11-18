from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def signup_view(request, *args, **kwargs):
    return render(request, "signup.html", {})


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})
