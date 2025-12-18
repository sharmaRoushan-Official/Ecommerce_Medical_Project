from django.shortcuts import render

# Create your views here.


def viewHome(request):
    resp = render(request,'novenaApp/home.html')
    return resp

