from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class UserInfo(models.Model):
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100, blank=False)
    roll_no=models.CharField(max_length=100, blank=False,primary_key=True)
    dob=models.DateTimeField(default=timezone.now, editable=True)
    user_name=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(default=' ')
    password1=models.CharField(max_length=100, blank=False)
    password2=models.CharField(max_length=100, blank=False)

def __str__(self):
    return self.first_name