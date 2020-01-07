from django.contrib import admin
from . models import UserInfo


class AdminUserInfo(admin.ModelAdmin):
    model = UserInfo
    list_display = ('first_name','last_name','roll_no','dob','user_name', 'email')


admin.site.register(UserInfo, AdminUserInfo)
