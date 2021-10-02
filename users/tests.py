from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your tests here.

class UserViewTestCase(TestCase):
    
    def setUp(self):
        
        User.objects.create(username="user1", password=make_password('1234'), email="user1@example.com")

    
    
    
    def test_index_view_with_authentication(self):
        
        
        c = Client()
        user = User.objects.get(username="user1")
        c.force_login(user)
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)
        
    
    def test_index_view_without_authentication(self):
        
        
        c = Client()
        user = User.objects.get(username="user1")
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)
        
        
    def test_login_success(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.post(reverse('users:login'), {'username': 'user1', 'password': '1234'})
        self.assertEqual(response.status_code, 302)
        
    def test_login_unsuccess(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.post(reverse('users:login'), {'username': 'user1', 'password': '123'})
        self.assertEqual(response.status_code, 200)