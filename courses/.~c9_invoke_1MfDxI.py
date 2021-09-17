from django.contrib import admin

# Register your models here.
from .models import Course, Student

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "semester", "year", "amount", "status")


    
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)




