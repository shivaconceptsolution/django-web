from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome in Teacher APP")

def assignment(request):
    return HttpResponse("Welcome in assignment page")

def login(request):
    return HttpResponse("Welcome in login page")

def report(request):
    return HttpResponse("Welcome in report page")