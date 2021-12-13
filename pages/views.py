from django.contrib.admin import decorators
from django.shortcuts import render, redirect
from users.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.views.generic import ListView, DetailView


def signup_view(request, *args, **kwargs):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account Has Been Created! ')
            return redirect('login')

    context = {'form': form}
    return render(request, "signup.html", context)


# def home_view(request, *args, **kwargs):
#     context = {
#         'posts': Post.objects.all(),
#     }
#     return render(request, "home.html", context)


@login_required
def profile_view(request, *args, **kwargs):
    context = {
        'title': 'My Profile',
    }
    return render(request, "profile.html", context)


class PostListView(ListView):
    model = Post
    template_name ='home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name='posts.html'