from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class UserInfo(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100)
    dob=models.DateField(auto_now=True)
    user_name=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(default=' ')
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

def __str__(self):
    return self.first_name