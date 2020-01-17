from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path("",views.register, name = 'register'),
    path('login/register/',views.register, name = 'register'),
    path('login/',views.login, name='blog-login'),    
    path('loginForm/',views.loginForm, name="blog-loginForm"),
    path('formSubmit/OTPresend/',views.OTPresend, name='blog-OTPresend'),
    path('formSubmit/', views.formSubmit,name = 'blog-formSubmit'),
    path('home/', views.home,name = "blog-home"),
    path('OTPpage/', views.OTPpage,name = "blog-otp"),
    path('SubmitOTP/', views.SubmitOTP, name="blog-SubmitOTP"),
    path('forgotPassword/', views.forgotPassword, name = "blog-forgotPassword"),
    path('forgotPasswordPage/', views.forgotPasswordPage, name = "blog-forgotPasswordPage"),
    path('PasswordReset/', views.PasswordReset, name = "blog-PasswordReset"),
    path('login/forgotPasswordPage/', views.forgotPasswordPage, name = "blog-forgotPasswordPage"),

]