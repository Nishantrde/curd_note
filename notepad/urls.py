from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("shadow.urls")),
    path('notepad/',include("note.urls"))
]

