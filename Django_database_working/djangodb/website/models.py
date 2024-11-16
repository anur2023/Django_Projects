from django.db import models

# Create your models here.
class Members(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwd =models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.fname + " "+self.lname

