from django.urls import path

from . import views


app_name = "registration"
urlpatterns = [

    path('', views.index, name="index"),
    path('home/', views.index, name="index"),
    

    ]