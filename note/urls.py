from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name="sign_in"),
    path('login', views.login_page, name="login_page"),
    path('logout', views.log_out, name="log_out"),
    path('verify/<token>', views.verify, name="verify"),
    path('note', views.notepad, name="notes"),
    path('diary', views.diary, name="diary"),
    path('user_note', views.note_, name="note"),
    path('save', views.save, name="save"),
    path('user_note', views.note_, name="note"),
    path('delete', views.delete, name="delete"),
    path('update', views.update, name="update"),
]

