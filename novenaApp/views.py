from django.shortcuts import render
from novenaApp.models import contactModel
from django.http import HttpResponse
from django.shortcuts import redirect

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
    if request.method == "POST":
        contact = contactModel.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            subject=request.POST.get("subject", ""),
            phoneNo=request.POST.get("phone", ""),
            message=request.POST.get("message", ""),
        )
        
        return render(request,'novenaApp/contactSuccess.html',{'name':contact.name})

    return render(request, "novenaApp/contact.html")

