from django.db import models

class First(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    # address = models.TextField(blank = True, null = True)
    # email = models.EmailField()
    # img = models.ImageField()
    # file =  models.FileField()
    def __str__(self):
        return self.name    
