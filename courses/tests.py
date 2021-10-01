from django.test import TestCase

# Create your tests here.

from .models import Course
from django.contrib.auth.models import User

class CourseTestCase(TestCase):
    
    def setUp(self):
        
        course1 = Course.objects.create(code="AAA", name="AAA", semester="AAA", year="AAA", amount=2, status=1, count=0)
        
    def test_course_available(self):
        """ is_course_available should be True """
        
        course = Course.objects.first()
        
        self.assertTrue(course.is_course_available())
        
        
    def test_course_not_available(self):
        """ is_course_available should be False """
        
        user1 = User.objects.create(username="user1", password="1234", email="user1@example.com")
        user2 = User.objects.create(username="user2", password="1234", email="user1@example.com")
        
        course = Course.objects.first()
        course.registered_course.add(user1)
        course.registered_course.add(user2)
        
        self.assertFalse(course.is_course_available())
        