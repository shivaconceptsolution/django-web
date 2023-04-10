from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    if request.method=="POST":
            a = request.POST["txtnum1"]
            b = request.POST["txtnum2"]
            c = int(a)+int(b)
            return HttpResponse("Result is "+str(c))
    else:         
      return render(request,"addition.html")
def prime(request):
    if request.method=="POST":
      num=int(request.POST["num"])
      s=''
      for i in range(2,num):
        if num%i==0:
            s='not prime'
            break
      else:
        s='prime'
      return HttpResponse(s) 
    else:
        return render(request,"prime.html")            

def fibonacci(request):
    a=-1
    b=1
    res=''
    for i in range(10):
        c=a+b
        res+=str(c) + " "
        a=b
        b=c
    return HttpResponse(res)    

