from django.contrib import admin

from .models import *
# Register your models here.

# admin.site.register(contactModel)

@admin.register(contactModel)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phoneNo', 'message')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'doctor', 'appointment_date', 'appointment_time', 'phone_number','message','is_active', 'created_at')
    list_filter = ('department', 'doctor', 'appointment_date', 'is_active')
    search_fields = ('full_name', 'phone_number', 'doctor')

@admin.register(SubstribeFooter)
class SubstribeFooterAdmin(admin.ModelAdmin):
    list_display = ('email',)   

# admin.site.register(Appointment)
# admin.site.register(SubstribeFooter)      

@admin.register(singleBlogModel)
class singleBlogModel(admin.ModelAdmin):
    list_display = ('name','email','message')