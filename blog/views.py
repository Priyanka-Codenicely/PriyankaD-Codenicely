from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserInfo
# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def register(request):
    return render(request,'blog/signup.html')


def formSubmit(request):
    print('inside submit api')
    if request.method == 'POST':
        first_name=request.POST["first_name"]
        print(first_name)
        last_name=request.POST["last_name"]
        roll_no=request.POST["roll_no"]
        
        user_name=request.POST["user_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        user_info=UserInfo(first_name=first_name,last_name=last_name,roll_no=roll_no,user_name=user_name,email=email,password1=password1,password2=password2)
        user_info.save()
    return render(request,'blog/home.html')
