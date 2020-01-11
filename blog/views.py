from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import UserInfo
from django.contrib.auth import authenticate 
'''
from .form import UserForm
# Create your views here.
'''
def home(request):
    return render(request, 'blog/home.html')

def register(request):
    return render(request,'blog/signup.html')

def blank(request):
    return render(request,'blog/blank.html')

def login(request):
    return redirect('blog/home.html')

def signup(request):
    response = redirect('blog/signup.html')
    return response

def formSubmit(request):
    context = {}
    print('inside submit api')
    if request.method == 'POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        roll_no=request.POST["roll_no"]       
        user_name=request.POST["user_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        if UserInfo.objects.filter(roll_no=roll_no).exists():
            context['err_msg']='The Roll Number you entered already exists.'
            return render(request,'blog/signup.html',context)
        elif UserInfo.objects.filter(email=email).exists():
            context['err_msg2']='The Email id you entered already exists.'
            return (request,'blog/signup.html',context)
        else:
            user_info=UserInfo(first_name=first_name,last_name=last_name,roll_no=roll_no,user_name=user_name,email=email,password1=password1)
            user_info.save()
            return render(request,'blog/otp.html')

def loginForm(request):
    print('hello mate')
    context = {}
    if request.method == 'POST':
        print("i'm here")
        email=request.POST.get("Email")
        print('email', email)
        password=request.POST.get("password")
        print('password',password)
        if UserInfo.objects.filter(email=email).exists():
            if UserInfo.objects.filter(email=email,password1=password).exists():
                return render(request,'blog/blank.html')
            else:
                context['err_msg3']="The Password you entered doesn't match with the Email "
                return render(request, 'blog/home.html',context)
        else:
            context['err_msg4']="The Email id you entered doesn't exist.Please Sign Up "
            return render(request,'blog/signup.html',context)
        
            