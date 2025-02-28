from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from connections.models import Connection  # Import the connection model
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def feed(request):
    user = request.user  # Get logged-in user

    # ✅ Fetch IDs of connected users (including mutual connections)
    connected_user_ids = Connection.objects.filter(from_user=user).values_list(
        "to_user_id", flat=True
    )

    # ✅ Include user's own posts in the feed
    posts = Post.objects.filter(user_id__in=connected_user_ids).order_by("-created_at")

    return render(request, "posts/feed.html", {"posts": posts})


@login_required
def profile(request, user_id):
    # Get the user object
    user = get_object_or_404(User, id=user_id)

    # Get the user's personal posts
    posts = Post.objects.filter(user=user).order_by("-created_at")

    return render(request, "profile.html", {"user": user, "posts": posts})


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the current user to the post
            post.save()
            return redirect("feed")  # Redirect to the feed after posting
    else:
        form = PostForm()

    return render(request, "posts/add_post.html", {"form": form})


@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # ✅ Fetch connections (both ways)
    connections = Connection.objects.filter(user=user).select_related("connected_user")

    # ✅ Extract connected users
    connected_users = [connections.connected_user for conn in connections]

    # ✅ Fetch user's posts
    posts = Post.objects.filter(user=user).order_by("-created_at")

    return render(
        request,
        "accounts/profile.html",
        {
            "user": user,
            "posts": posts,
            "connections": connected_users,  # ✅ Pass connections to template
            "connections_count": len(connected_users),  # ✅ Pass total count
        },
    )
