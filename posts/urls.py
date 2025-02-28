from django.urls import path
from posts.views import feed, add_post

urlpatterns = [
    path("feed/", feed, name="feed"),
    path("add-post/", add_post, name="add_post"),
]
