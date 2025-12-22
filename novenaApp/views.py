from django.shortcuts import render
from novenaApp.models import contactModel
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Appointment

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
    if request.method == "POST":
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")

        Appointment.objects.create(
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            full_name=full_name,
            phone_number=phone_number,
            message=message
        )

        return render(request,"novenaApp/appointment_success.html")

    return render(request, "novenaApp/appoinment.html")



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


