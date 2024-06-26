from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prac/', include("shadow.urls")),
    path('', include("note.urls", namespace="main_note")),  # Include the note URLs
    path("google_sso/", include("django_google_sso.urls", namespace="django_google_sso")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
