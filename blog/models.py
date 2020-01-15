from django.db import models
from django.utils import timezone
from datetime import date

class DateInput(models.DateField):
    input_type='date'

# Create your models here.
class UserInfo(models.Model):
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100, blank=False)
    roll_no=models.PositiveIntegerField(primary_key=True)
    dob=models.DateTimeField(null=False)
    user_name=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(default=' ')
    password1=models.CharField(max_length=100, blank=False)
    otp=models.CharField(max_length=4, blank=False)
    user_status_verified = models.BooleanField(default=False)

def __str__(self):
    return self.roll_no

class StatusManager(models.Manager):
    def generateStatus(self,status):
        status = self.create(status=status)
        # do something with the book
        return status
"""
class UserInfoDate(models.Model):
    class meta:"""