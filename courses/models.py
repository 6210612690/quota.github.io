from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Course(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    semester = models.CharField(max_length=1)
    year = models.CharField(max_length=4)
    amount = models.IntegerField()
    status = models.IntegerField(default=1)
    registered_course = models.ManyToManyField(User, blank=True, related_name="students")
    count = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return f"{self.id}: {self.code} {self.name} {self.semester}/{self.year} {self.amount} status-{self.status}"
        
    def is_course_available(self):
        return self.registered_course.count() < self.amount
