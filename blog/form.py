from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name','roll_no','dob','user_name', 'email', 'password1','password1')