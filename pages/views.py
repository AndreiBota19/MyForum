from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from posts.models import Post


# Create your views here.

def login_view(request, *args, **kwargs):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Your Username and Password are Incorrect!')

    context = {}
    return render(request, "login.html", context)


def signup_view(request, *args, **kwargs):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created! ')
            return redirect('login')

    context = {'form': form}
    return render(request, "signup.html", context)


def logout_view(request, *args, **kwargs):
    return redirect('login')


def home_view(request, *args, **kwargs):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "home.html", context)
