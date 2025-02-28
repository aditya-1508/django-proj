from django.db import models
from django.contrib.auth.models import User

from django.conf import settings  # ✅ Correct way to reference User model

from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    VISIBILITY_CHOICES = [
        ("public", "Public"),
        ("private", "Private"),
        ("connections", "Connections Only"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="Default Post Text")  # 👈 Add default value
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(
        max_length=20, choices=VISIBILITY_CHOICES, default="public"
    )  # ✅ Ensure this exists

    def __str__(self):
        return f"{self.user.username}: {self.text[:30]}"


class Connection(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="connections"
    )
    connected_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="connected_to"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "connected_user")  # ✅ Ensure unique connections

    def __str__(self):
        return f"{self.user} -> {self.connected_user}"
