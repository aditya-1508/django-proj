from django.contrib import admin  # ✅ Add this line
from django.urls import path, include
from posts.views import feed  # ✅ Import the feed view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("connections/", include("connections.urls")),
    path("search/", include("search.urls")),
    path("posts/", include("posts.urls")),  # ✅ Ensure this line exists
    path("", feed, name="feed"),  # ✅ Add this line if missing
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
