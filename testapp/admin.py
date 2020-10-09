from django.contrib import admin
from testapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','dob','profile_pic']

admin.site.register(Student,StudentAdmin)
