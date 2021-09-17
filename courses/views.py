from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.



from .models import Course

    


def index(request):
    return render(request, "courses/index.html", {
        "courses": Course.objects.all()
    })

def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    num = course.amount - course.count
    return render(request, "courses/course.html",{
        "course": course,
        "students": course.registered_course.all(),
        "num": num,
    })

    
    

        
def register(request, course_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("register:home"))
            
    course = get_object_or_404(Course, pk=course_id)
    if request.user not in course.registered_course.all():
        course.registered_course.add(request.user)
        counter = Course.objects.get(id=course_id)
        counter.count += 1
        counter.save()
        return HttpResponseRedirect(reverse("courses:course", args=(course_id,)))




def remove(request, course_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("register:home"))
    course = get_object_or_404(Course, pk=course_id)
    if request.user in course.registered_course.all():
        course.registered_course.remove(request.user)
        counter = Course.objects.get(id=course_id)
        counter.count -= 1
        counter.save()
        return HttpResponseRedirect(reverse("courses:course", args=(course_id,)))
        
        
    