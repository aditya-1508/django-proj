from django.db import models
from accounts.models import CustomUser  # Ensure it's your CustomUser model


class Connection(models.Model):
    from_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="connections_sent"
    )
    to_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="connections_received"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} → {self.to_user}"
