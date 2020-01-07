from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.register, name = 'register'),
    path("home/register",views.register, name = 'register'),
    path("home/",views.home, name="blog-home"),    
    path("home/home/",views.home, name="blog-home"), 
    path('formSubmit/', views.formSubmit,name = 'formSubmit')
]
