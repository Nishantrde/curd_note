from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name="sign_in"),
    path('login', views.index, name="index"),
    path('note', views.notepad, name="notes"),
    path('diary', views.diary, name="diary"),
    path('user_note', views.note_, name="note"),
    path('save', views.save, name="save"),
    path('user_note', views.note_, name="note"),
    path('delete', views.delete, name="delete"),
]

