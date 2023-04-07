from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    a,b=100,2
    c=a+b
    return HttpResponse("result is "+str(c))
def prime(request):
    num=6
    s=''
    for i in range(2,num):
        if num%i==0:
            s='not prime'
            break
    else:
        s='prime'
    return HttpResponse(s)           

