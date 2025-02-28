from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from posts.models import Post  # ✅ Import Post model
from .models import Connection
from django.contrib.auth.decorators import login_required


@login_required
def add_connection(request, user_id):
    to_user = get_object_or_404(
        CustomUser, id=user_id
    )  # ✅ Fetch the user to connect with
    from_user = request.user  # ✅ Get the logged-in user

    # ✅ Prevent duplicate connections
    if not Connection.objects.filter(from_user=from_user, to_user=to_user).exists():
        Connection.objects.create(from_user=from_user, to_user=to_user)

    return redirect("profile", user_id=user_id)  # Redirect to the user's profile


def user_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)  # ✅ Correct model
    posts = Post.objects.filter(user=user).order_by(
        "-created_at"
    )  # ✅ Fetch posts by user

    return render(request, "accounts/profile.html", {"user": user, "posts": posts})
