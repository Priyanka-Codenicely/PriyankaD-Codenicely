from django.contrib import admin
from . models import UserInfo, Note


class AdminUserInfo(admin.ModelAdmin):
    model = UserInfo
    list_display = ('first_name','last_name','roll_no','dob','user_name', 'email')

class AdminNotes(admin.ModelAdmin):
    model = Note
    list_display = ['noteId','title', 'description','datetime', 'userid']


admin.site.register(UserInfo)
admin.site.register(Note)
