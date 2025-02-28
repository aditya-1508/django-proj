from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "visibility", "created_at")  # ✅ Show in list
    search_fields = ("user__username", "text")  # ✅ Enable search
    list_filter = ("visibility", "created_at")  # ✅ Enable filtering
