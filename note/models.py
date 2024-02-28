from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length = 20)
    user_id = models.IntegerField()
    def __str__(self):
        return str(self.user_name)
    
class Notes(models.Model):
    user_id = models.IntegerField()
    user_notes_title = models.CharField(max_length = 20, default="Title")
    user_notes = models.CharField(max_length = 2500)
    def __str__(self):
        return str(self.user_id)

