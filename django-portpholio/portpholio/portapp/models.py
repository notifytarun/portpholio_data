from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=500,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    