from django.shortcuts import render
from novenaApp.models import contactModel,SubstribeFooter,singleBlogModel
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Appointment
from datetime import datetime, date

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


from datetime import datetime, date

def viewAppoinment(request):
    if request.method == "POST":
        # Get all form data
        department = request.POST.get("department", "").strip()
        doctor = request.POST.get("doctor", "").strip()
        appointment_date = request.POST.get("appointment_date", "").strip()
        appointment_time = request.POST.get("appointment_time", "").strip()
        full_name = request.POST.get("full_name", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        message = request.POST.get("message", "").strip()

        # Validation errors list
        errors = []

        # Validate department
        if not department or department == "Choose Department":
            errors.append("Please select a department.")

        # Validate doctor
        if not doctor or doctor == "Select Doctors":
            errors.append("Please select a doctor.")

        # Validate appointment date
        if not appointment_date:
            errors.append("Please select an appointment date.")
        else:
            try:
                date_obj = datetime.strptime(appointment_date, "%Y-%m-%d").date()
                # Check if date is not in the past
                if date_obj < date.today():
                    errors.append("Appointment date cannot be in the past.")
            except ValueError:
                errors.append("Invalid date format.")

        # Validate appointment time
        if not appointment_time:
            errors.append("Please select an appointment time.")

        # Validate full name
        if not full_name:
            errors.append("Please enter your full name.")
        elif len(full_name) < 3:
            errors.append("Name must be at least 3 characters long.")

        # Validate phone number
        if not phone_number:
            errors.append("Please enter your phone number.")
        elif not phone_number.replace("+", "").replace("-", "").replace(" ", "").isdigit():
            errors.append("Phone number must contain only digits.")
        elif len(phone_number.replace("+", "").replace("-", "").replace(" ", "")) < 10:
            errors.append("Phone number must be at least 10 digits.")

        # If there are errors, return to form with errors
        if errors:
            return render(request, "novenaApp/appoinment.html", {
                'errors': errors,
                'department': department,
                'doctor': doctor,
                'appointment_date': appointment_date,
                'appointment_time': appointment_time,
                'full_name': full_name,
                'phone_number': phone_number,
                'message': message
            })

        # Check for duplicate appointments
        existing_appointment = Appointment.objects.filter(
            phone_number=phone_number,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists()

        if existing_appointment:
            return render(request, "novenaApp/appoinment.html", {
                'errors': ['You already have an appointment scheduled at this date and time.'],
                'department': department,
                'doctor': doctor,
                'appointment_date': appointment_date,
                'appointment_time': appointment_time,
                'full_name': full_name,
                'phone_number': phone_number,
                'message': message
            })

        # Create appointment
        try:
            Appointment.objects.create(
                department=department,
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                full_name=full_name,
                phone_number=phone_number,
                message=message
            )

            return render(request, "novenaApp/appointment_success.html", {
                'name': full_name
            })

        except Exception as e:
            return render(request, "novenaApp/appoinment.html", {
                'errors': [f'Error creating appointment: {str(e)}'],
                'department': department,
                'doctor': doctor,
                'appointment_date': appointment_date,
                'appointment_time': appointment_time,
                'full_name': full_name,
                'phone_number': phone_number,
                'message': message
            })

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


def viewSubscribeFooter(request):
    if request.method == "POST":
        subscribe = SubstribeFooter.objects.create(
            email=request.POST.get("email", "")
        )
        return render(request,"novenaApp/subscribe_success.html")
    

# singleBlogPage

def viewSingleBlog(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        
        # Check if email already exists
        if singleBlogModel.objects.filter(email=email).exists():
            return render(request, "novenaApp/singleBlog.html", {
                'error': 'You have already commented with this email.'
            })
        
        # Create the comment only if email doesn't exist
        message = singleBlogModel.objects.create(
            name=request.POST.get("name", ""),
            email=email,
            message=request.POST.get("comment", "")
        )
        return render(request, "novenaApp/messageSentSuccess.html")
    
    return render(request, "novenaApp/singleBlog.html")



