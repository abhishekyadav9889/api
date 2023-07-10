from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','fast_name','last_Name','roll_No','ctye']