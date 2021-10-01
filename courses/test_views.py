from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max

from .models import Course
from django.contrib.auth.models import User

class CourseViewTestCase(TestCase):
    
    def setUp(self):
        course = Course.objects.create(code="AAA", name="AAA", semester="AAA", year="AAA", amount=2, status=1, count=0)
        
        user = User.objects.create(username="user", password="1234", email="user@example.com")
        
        course.registered_course.add(user)
        
        
    def test_index_view_status_code(self):
        """check status code"""
        
        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual (response.status_code, 200)
        
        
    def test_index_view_context(self):
        """check amount from list"""
        
        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual (response.context['courses'].count(), Course.objects.count())
        
        
    def test_valid_course_page(self):
        """check data from course"""
        
        c = Client()
        c1 = Course.objects.first()
        response = c.get(reverse('courses:course', args=(c1.id,)))
        self.assertEqual (response.status_code, 200)
        
    def test_invalid_course_page(self):
        """check courseid from page"""
        
        max_id = Course.objects.all().aggregate(Max("id"))['id__max']
        
        c = Client()
        response = c.get(reverse('courses:course', args=(max_id+1,)))
        self.assertEqual (response.status_code, 404)
        
        
    def test_guest_user_cannot_register_course(self):
        """guest cannot register"""
        user = User.objects.create(username="user2", password="1234", email="user2@example.com")
        c1 = Course.objects.first()
        
        c = Client()
        response = c.get(reverse('courses:course', args=(c1.id,)))
        self.assertEqual (c1.registered_course.count(), 1)
        
    
    def test_authenticated_user_register_course(self):
        
        user = User.objects.create(username="user2", password="1234", email="user2@example.com")
        c1 = Course.objects.first()
        
        c = Client()
        c.force_login(user)
        response = c.get(reverse('courses:register', args=(c1.id,)))
        self.assertEqual (c1.registered_course.count(), 2)
        
        

        
    
    
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        