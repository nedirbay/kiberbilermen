from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, SignupForm
from .models import UserProfile


def register(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user)
            login(request, user)
            return redirect("accounts:profile")
    else:
        form = SignupForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("accounts:profile")
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main:home")


@login_required
def profile(request):
    profile_obj, _ = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "accounts/profile.html", {"profile": profile_obj})
