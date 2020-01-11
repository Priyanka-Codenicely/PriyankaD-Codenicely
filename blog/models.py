from django.db import models
from django.utils import timezone
from datetime import date

class DateInput(models.DateField):
    input_type='date'

# Create your models here.
class UserInfo(models.Model):
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100, blank=False)
    roll_no=models.CharField(max_length=100, blank=False,primary_key=True)
    dob=models.DateTimeField(null=False)
    user_name=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(default=' ')
    password1=models.CharField(max_length=100, blank=False)
    password2=models.CharField(max_length=100, blank=False)

def __str__(self):
    return self.first_name
"""
class UserInfoDate(models.Model):
    class meta:"""