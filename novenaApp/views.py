from django.shortcuts import render

# Create your views here.


def viewHome(request):
    resp = render(request,'novenaApp/home.html')
    return resp

def viewAbout(request):
    resp = render(request, 'novenaApp/about.html')
    return resp
def viewService(reqeust):
    resp = render(reqeust,"novenaApp/service.html")
    return resp
