from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):

    return HttpResponse('This is the registration page!')


def my_login(request):
    return HttpResponse('This is the login page')

def home(request):
    return render(request, 'index.html')

