from django.urls import path
from .views import signup_view, login_view, logout_view, home  # ✅ Import home
from .views import upload_profile_picture

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "upload-profile-picture/", upload_profile_picture, name="upload_profile_picture"
    ),
    path("home/", home, name="home"),  # ✅ Now this will work
]
