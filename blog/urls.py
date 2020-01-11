from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.register, name = 'register'),
    path("home/register",views.register, name = 'register'),
    path("home/",views.home, name="blog-home"),    
    path("home/home/",views.home, name="blog-home"), 
    path('formSubmit/', views.formSubmit,name = 'formSubmit'),
    path('home/loginForm/', views.loginForm, name='loginForm'),
    path('blank/', views.blank,"blog-blank"),
]
"""
CLASS OTPAdmin(OTPAdminSite):
    pass

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

admin_site= OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)
"""