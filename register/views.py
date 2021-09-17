from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'registration/signup.html',{})
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})
    

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "courses/welcome.html", )

def home(request): 
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "courses/home.html", )