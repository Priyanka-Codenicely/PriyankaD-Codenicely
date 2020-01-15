from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path("",views.register, name = 'register'),
    path('login/register/',views.register, name = 'register'),
    path('login/',views.login, name='blog-login'),    
    path('formSubmit/OTPresend/',views.OTPresend, name='blog-OTPresend'),
    path('formSubmit/', views.formSubmit,name = 'formSubmit'),
    path('home/', views.home,name = "blog-home"),
    path('OTPpage/', views.OTPpage,name = "blog-otp"),
    path('formSubmit/SubmitOTP/', views.SubmitOTP, name="blog-SubmitOTP"),
    path('formSubmit/OTPresend/SubmitOTP/', views.SubmitOTP, name="blog-SubmitOTP"),

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