from django.contrib import admin
from .models import Connection


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ("get_from_user_phone", "get_to_user_phone", "created_at")
    search_fields = ("from_user__phone", "to_user__phone")
    list_filter = ("created_at",)

    def get_from_user_phone(self, obj):
        return obj.from_user.phone  # ✅ Correct field name

    def get_to_user_phone(self, obj):
        return obj.to_user.phone  # ✅ Correct field name

    get_from_user_phone.short_description = "From User"
    get_to_user_phone.short_description = "To User"
