from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_filter = ('University', 'Faculty', 'collegeDepartment', 'graduationYear', 'haveCar')
    search_fields = ['firstName', 'middleName', 'lastName', 'Mobile', 'collegeID', 'nationalID', 'email']
    list_display = ['firstName', 'middleName', 'Mobile', 'email', 'Faculty', 'graduationYear']


admin.site.register(Member,MemberAdmin)  # to add our model to admin panel
