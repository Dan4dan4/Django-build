from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Here we create a function that takes a request and gives response also known as a request handler

def say_hello(request):
    # in this function we can pull data from db, transform stuff, send emails etc
    return HttpResponse('Hello World')