from django.shortcuts import render
from django.http import HttpResponse
def swapcode(request):
    if request.method=="POST":
         a,b=request.POST['txtnum1'],request.POST['txtnum2']
         a,b=b,a
         res = "a="+ str(a) + " b =" + str(b)
         return render(request,"swap.html",{"res":res})
    else:
        return render(request,"swap.html")     
