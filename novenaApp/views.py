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


def viewDepartment(request):
    resp = render(request,'novenaApp/department.html')
    return resp

def viewSingleDepartment(request):
    resp = render(request,'novenaApp/singleDepartment.html')
    return resp


def viewDoctors(request):
    resp = render(request,'novenaApp/doctors.html')
    return resp

def viewSingleDoctor(reqeust):
    resp = render(reqeust,"novenaApp/singleDoctor.html")
    return resp

def viewAppoinment(request):
    resp = render(request,"novenaApp/appoinment.html")
    return resp


def viewBlog(request):
    resp = render(request, 'novenaApp/blog.html')
    return resp

def viewSingleBlog(request):
    resp  = render(request,'novenaApp/singleBlog.html')
    return resp

def viewContact(request):
    resp = render(request,"novenaApp/contact.html")
    return resp
