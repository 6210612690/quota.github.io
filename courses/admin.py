from django.contrib import admin

# Register your models here.
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "semester", "year", "amount", "status")


    
admin.site.register(Course, CourseAdmin)





