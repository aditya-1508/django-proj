from django.urls import path
from .views import user_profile, add_connection


urlpatterns = [
    path("profile/<int:user_id>/", user_profile, name="profile"),
    path(
        "connect/<int:user_id>/", add_connection, name="add_connection"
    ),  # ✅ Fixing the name
]
