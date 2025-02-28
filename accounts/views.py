from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required  # ✅ Import this
from accounts.forms import (
    SignupForm,
    ProfilePictureForm,
)  # ✅ Ensure these imports exist
from accounts.models import CustomUser  # ✅ Ensure you import CustomUser


@login_required
def upload_profile_picture(request):
    if request.method == "POST":
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(
                "profile", user_id=request.user.id
            )  # Redirect to profile page
    else:
        form = ProfilePictureForm(instance=request.user)

    return render(request, "accounts/upload_profile_picture.html", {"form": form})


def home(request):
    return render(request, "accounts/home.html")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        user = authenticate(request, username=phone, password=password)
        if user:
            login(request, user)
            return redirect("feed")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
