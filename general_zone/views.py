from django.shortcuts import render, redirect,HttpResponse
from .models import *
from admin_zone.models import *
from django.contrib.auth.views import LoginView
from django.urls import *


def index(request):
    Books = Book.objects.all()
    return render(request, 'index.html',{'Books':Books})

def user_login(request):
    return render(request, 'user_login.html')

def admin_login(request):
    return render(request, 'admin_login.html')


class CustomLoginView(LoginView):
    template_name = 'admin_login.html'   
    def get_success_url(self):
        # Customize the URL where the user is redirected after a successful login
        return reverse_lazy('admin_home')


