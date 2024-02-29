from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("shadow.urls")),
    path('notepad/',include("note.urls"))
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

