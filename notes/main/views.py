from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import Profile
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, "pages/home.html", {})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('profile')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, "pages/logged_out.html",{})


def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("profile")
    else:
        form = ProfileForm
        if 'username' in request.GET:
            username = request.GET['username']
            return redirect(f'/profile{username}')
        return render(request, "pages/profile.html", {'form':form})


@login_required
def user_profile(request):
    user = User.objects.get
    return render(request, "pages/notes.html", {'user':user})


def sign_up(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            return render(request, 'pages/profile.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'pages/register.html', {'user_form': user_form})






