from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def top(request):
    return HttpResponse("Hello")