from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

# ✅ Custom User Admin Configuration
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "phone", "email", "is_staff", "is_active", "date_joined")
    search_fields = ("phone", "email")
    ordering = ("-date_joined",)
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("phone", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)  # ✅ Register CustomUser
