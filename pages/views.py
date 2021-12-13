from django.contrib.admin import decorators
from django.shortcuts import render, redirect
from users.forms import CreateUserForm, ProfileUpdateForm, UserUpdateForm
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


@login_required
def profile_view(request, *args, **kwargs):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'My Profile',
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "profile.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts.html'
