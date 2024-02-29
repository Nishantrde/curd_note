from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_in', views.sign_in, name="sign_in"),
    path('note', views.notepad, name="notes"),
    path('save', views.save, name="save"),
    path('diary', views.diary, name="diary"),
    path('user_note', views.note_, name="note"),
]

