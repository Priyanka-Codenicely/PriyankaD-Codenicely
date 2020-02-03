from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import UserInfo, Note
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
import math, random 
import datetime

'''
from .form import UserForm
# Create your views here.
'''
def login(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request,'blog/signup.html')


def home(request):
    context = {}
    if 'username' in request.session:
        username = request.session.get('username')
        user = UserInfo.objects.get(user_name=username)
        print('hey displayNote')
        rollno = user.roll_no
        print(rollno)
        notes = Note.objects.filter(userid=rollno)
        return render(request, 'blog/home.html', {'notes':notes} ,context)

    else:
        context['login']='Please Login'
        return render(request,'blog/login.html', context)

def OTPpage(request):
    return render(request, 'blog/otp.html') 

  
def generateOTP() : 
  
    digits = "0123456789"
    otp = "" 
  
    for i in range(4) : 
        otp += digits[math.floor(random.random() * 10)] 
    return otp 
  

def signup(request):
    response = redirect('blog/signup.html')
    return response

def formSubmit(request):
    context = {}
    print('inside submit api')
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        dob=request.POST.get("dob")
        print(dob)
        roll_no=request.POST.get("roll_no")      
        user_name=request.POST.get("user_name")
        email=request.POST.get("email")
        email = email.lower()
        password1=request.POST.get("password1")
        if UserInfo.objects.filter(roll_no=roll_no).exists():
            context['err_msg']='The Roll Number you entered already exists.'
            return render(request,'blog/signup.html',context)
        elif UserInfo.objects.filter(email=email).exists():
            context['err_msg2']='The Email id you entered already exists.'
            return render(request,'blog/signup.html',context)
        elif UserInfo.objects.filter(user_name=user_name).exists():
            context['err_msg2']='The User Name you entered already exists.'
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
            message= 'Welcome to Easy Notes Maker, %s is your OTP' %otp
            from_email= settings.EMAIL_HOST_USER
            to_list=[user_info.email]
            print("mail",to_list)
            send_mail(subject,message,from_email,to_list)
            context['email']=user_info.email
            request.session['username']=user_info.user_name            
            print('email', context['email'])
            return render(request,'blog/otp.html',context)


def loginForm(request):
    print('hello mate')
    context = {}
    username = None
    if request.method == 'POST':
        print("i'm here")
        email=request.POST.get("Email")
        email = email.lower()
        print('email', email)
        password=request.POST.get("password")
        print('password',password)
        if UserInfo.objects.filter(email=email).exists():
            if UserInfo.objects.filter(email=email,password1=password).exists():
                print('it')
                user = UserInfo.objects.get(email=email,password1=password)
                if user.user_status_verified:
                    """if 'username' in request.session:
                        username=request.session.get('username')
                        return render(request,'blog/home.html', context)
                    else:"""
                    request.session['username']=user.user_name
                    return render(request,'blog/home.html')
                else:
                    context['otpverify'] = "Please verify your identity."
                    context['email'] = user.email
                    return render(request,'blog/otp.html',context)
            else:
                context['err_msg3']="The Password you entered doesn't match with the Email "
                return render(request, 'blog/login.html',context)
        else:
            context['err_msg4']="The Email id you entered doesn't exist.Please Sign Up "
            return render(request,'blog/signup.html',context)
    else:
        return render(request,'blog/home.html')



def logout(request):
    context = {}
    print('i reached at logout')
    del request.session['username']
    context['logout']='Please Log-in to Easy Notes Maker'
    return render(request,'blog/login.html')

def OTPresend(request):
    context = {}
    if request.method=='POST':
        email = request.POST.get('email')
        email = email.lower()
        print(email)
        otp = generateOTP()
        subject='OTP Resent'
        message= 'Welcome to Easy Notes Maker, %s is your new OTP' %otp
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
        email = email.lower()
        print(email)
        if UserInfo.objects.filter(email=email,otp=otp).exists():
            print('SubmitOTP exists')
            status = UserInfo.objects.get(email=email,otp=otp)
            status.user_status_verified = True
            status.save()
            context['name']=status.user_name
            request.session['username']=status.user_name
            print('name',context['name'])
            print('name',request.session['username'])
            return render(request,'blog/home.html',context)
        else:
            status = UserInfo.objects.get(email=email)
            status.user_status_verified = False
            status.save()
            context['email']=email
            context['err_msg5']="The OTP you entered is incorrect."
            return render(request, 'blog/otp.html', context)


def forgotPasswordPage(request):
    return render(request, 'blog/forgot_password.html')


def forgotPassword(request):
    context = {}
    if request.method=='POST':
        email = request.POST.get('email')
        email = email.lower()
        print(email)
        if UserInfo.objects.filter(email=email).exists():
            print('Its here')
            user = UserInfo.objects.get(email=email)
            newotp = generateOTP()
            user.otp = newotp
            print(user.otp)
            user.save()
            user.user_status_verified=False
            user.save()
            subject='OTP for resetting password'
            message= 'Welcome to Easy Notes Maker, %s is your New OTP' %newotp
            from_email= settings.EMAIL_HOST_USER
            to_list=[user.email]
            print("mail",to_list)
            send_mail(subject,message,from_email,to_list)
            context['email1']=user.email
            print('email', context['email1'])
            return render(request,'blog/passwordReset.html',context)
        else:
            context['err_msg4']="The Email id you entered doesn't exist.Please Sign Up "
            return render(request,'blog/forgot_password.html',context)



def PasswordReset(request):
    context = {}
    if request.method=='POST':
        email = request.POST.get('email1')
        email = email.lower()
        print(email)
        newotp = request.POST.get("otp")
        print(newotp)
        password1 = request.POST.get('password1')
        if UserInfo.objects.filter(email=email,otp=newotp).exists():
            print('PasswordReset exists')
            user = UserInfo.objects.get(email=email)
            user.user_status_verified= True
            user.save()
            user.password1 = password1
            user.save()
            context['name'] = user.user_name
            request.session['username']=user.user_name
            print('name',context['name'])
            print('name',request.session['username'])
            print('hey displayNote')
            user = UserInfo.objects.get(user_name=request.session['username'])
            rollno = user.roll_no
            print(rollno)
            notes = Note.objects.filter(userid=rollno)
            return render(request,'blog/home.html',{'notes':notes},context )
        else:
            context['email1']=email
            context['password_msg']="The OTP you entered didn't match"
            return render(request, 'blog/passwordReset.html',context)

def addNote(request):
    return render(request, 'blog/addNote.html')

def storeNote(request):
    print('I entered storenote')
    context={}
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        datetime = request.POST.get('datetime')
        print('datetime',datetime)
        print('Im in store notes')
        userid =  UserInfo.objects.get(user_name=request.session['username'])
        note = Note(title=title, description=description, datetime=datetime, userid=userid)
        note.save()
        print(note)
        context['saved'] = 'Note Saved'
        print('im at the bottom')
        print('hey displayNote inside storeNote')
        user = UserInfo.objects.get(user_name=request.session['username'])
        rollno = user.roll_no
        print(rollno)
        notes = Note.objects.filter(userid=rollno)
        return render(request, 'blog/home.html',{'notes':notes},context)

def EditNote(request,id):
    print('id', id)
    print(request.body)
    print('inside editresponse')
    if request.method=='GET':
        print('inside if condition')
        note = Note.objects.get(noteId=id)
        print('got instance',note)
        # note.title = request.GET.get('edittitle')
        title = request.GET.get('edit_title')
        print('1',title)
        note.save()
        print('2')
        note.description = request.GET.get('editdescription')
        print('3')
        note.save()
        print('4')
        user = UserInfo.objects.get(user_name=request.session['username'])
        print('5')
        rollno = user.roll_no
        print(rollno,rollno)
        notes = Note.objects.filter(userid=rollno)
        return render(request, 'blog/home.html',{'notes':notes})

def deleteNote(request,id):
    print('id', id)
    print('Im at delete note')
    obj = Note.objects.get(noteId=id)
    print('inside if condition')
    obj.delete()
    user = UserInfo.objects.get(user_name=request.session['username'])
    rollno = user.roll_no
    notes = Note.objects.filter(userid=rollno)
    return render(request, 'blog/home.html',{'notes':notes})

