from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create the following Python function named index. 
# Inside the function, we are returning a simple HTTP response.

def index(request):
    return HttpResponse("Hello, world!")

