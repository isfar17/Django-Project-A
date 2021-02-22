from django.db import models

# Create your models here.
class UserForm(models.Model):

    firstname=models.CharField(max_length=100,blank=True)
    lastname=models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=100,blank=True)

    def __str__(self):
        
        return self.firstname+'  '+self.lastname