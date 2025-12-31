from django.urls import path
from .views import *


urlpatterns = [
    path('home/',viewHome, name='home'), # http://127.0.0.1:8000/novapp/home/
    path('about/',viewAbout,name='about'), 
    path('service/',viewService,name="service"),
    path('department/',viewDepartment,name='department'),
    path('singleDepartment/',viewSingleDepartment,name='singleDepartment'),
    path('doctors/',viewDoctors,name='doctors'),
    path('singleDoctor/',viewSingleDoctor,name='singleDoctor'),
    path('appoinment/',viewAppoinment,name='appoinment'),
    path('blog/',viewBlog,name='blog'),
    path('singleBlog/',viewSingleBlog,name='singleBlog'),
    path('contact/',viewContact,name='contact'),
    path('subscribeFooter/',viewSubscribeFooter,name='subscribeFooter'),
    path('singleBlogComment/',viewSingleBlog,name="singleBlogComment"),
    path('dashboard/',dashboardView,name='dashboard'),
]
