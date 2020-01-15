from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import UserInfo,StatusManager
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
import math, random 

'''
from .form import UserForm
# Create your views here.
'''
def login(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request,'blog/signup.html')

def home(request):
    return render(request,'blog/home.html')

def OTPpage(request):
    return render(request, 'blog/otp.html') 

  
def generateOTP() : 
  
    digits = "0123456789"
    otp = "" 
  
    for i in range(4) : 
        otp += digits[math.floor(random.random() * 10)] 
    return otp 
  

def log_in(request):
    return redirect('blog/login.html')

def signup(request):
    response = redirect('blog/signup.html')
    return response

def formSubmit(request):
    context = {}
    print('inside submit api')
    if request.method == 'POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        dob=request.POST.get("dob")
        print(dob)
        roll_no=request.POST["roll_no"]       
        user_name=request.POST["user_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        if UserInfo.objects.filter(roll_no=roll_no).exists():
            context['err_msg']='The Roll Number you entered already exists.'
            return render(request,'blog/signup.html',context)
        elif UserInfo.objects.filter(email=email).exists():
            context['err_msg2']='The Email id you entered already exists.'
            return render(request,'blog/signup.html',context)
        else:
            otp = generateOTP()
            user_info=UserInfo(first_name=first_name,last_name=last_name,dob=dob,roll_no=roll_no,user_name=user_name,email=email,password1=password1,otp=otp)
            print(otp)
            print(user_info)
            user_info.save()
            """send_mail(subject,message,from_email,to_list, fail_silently=True)
            """   
            subject='OTP'
            message= '%s is your OTP' %otp
            from_email= settings.EMAIL_HOST_USER
            to_list=[user_info.email]
            print("mail",to_list)
            send_mail(subject,message,from_email,to_list)
            context['email']=user_info.email
            print('email', context['email'])
            return render(request,'blog/otp.html',context)


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
                return render(request,'blog/home.html')
            else:
                context['err_msg3']="The Password you entered doesn't match with the Email "
                return render(request, 'blog/login.html',context)
        else:
            context['err_msg4']="The Email id you entered doesn't exist.Please Sign Up "
            return render(request,'blog/signup.html',context)


def OTPresend(request):
    context = {}
    if request.method=='POST':
        email = request.POST.get('email')
        print(email)
        otp = generateOTP()
        subject='OTP Resent'
        message= '%s is your new OTP' %otp
        from_email= settings.EMAIL_HOST_USER
        to_list=[email]
        print("mail",to_list)
        send_mail(subject,message,from_email,to_list)
        resetotp = UserInfo.objects.get(email=email)
        resetotp.otp = otp
        resetotp.save()
        context['email']=email
        return render(request,'blog/otp.html',context)  


def SubmitOTP(request):
    context = {}
    if request.method=='POST':
        otp = request.POST.get("otp")
        print(otp)
        email = request.POST.get('email')
        print(email)
        if UserInfo.objects.filter(email=email,otp=otp).exists():
            print('this exists')
            status = UserInfo.objects.get(email=email,otp=otp)
            status.user_status_verified = True
            status.save()
            return render(request,'blog/home.html')
        else:
            status = UserInfo.objects.get(email=email)
            status.user_status_verified = False
            status.save()
            context['email']=email
            context['err_msg5']="The OTP you entered is incorrect."
            return render(request, 'blog/otp.html', context)