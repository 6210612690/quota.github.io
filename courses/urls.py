from django.urls import path

from . import views


app_name="courses"
urlpatterns = [
    
    path('', views.index, name="index"),
    path('<int:course_id>', views.course, name="course"),
    path('<int:course_id>/register', views.register, name="register"),
    path('<int:course_id>/remove', views.remove, name="remove"),
    

    
    ]