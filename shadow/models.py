from django.db import models

class First(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name  
      
class Second(First):
    i_d = models.IntegerField()
    
    def __str__(self):
        return self.name



