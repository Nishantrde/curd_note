from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    email_token = models.CharField(max_length = 200)
    is_verified = models.BooleanField(default = False)
    def __str__(self):
        return self.user.username

class Notes(models.Model):
    profile_name = models.CharField(default = "",max_length = 55)
    user_notes_title = models.CharField(max_length = 20, default="Title")
    user_notes = models.CharField(max_length = 2500)
    def __str__(self):
        return str(self.profile_name)

