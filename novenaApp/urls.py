from django.urls import path
from .views import *


urlpatterns = [
    path('home/',viewHome, name='home'), # http://127.0.0.1:8000/novapp/home/
    path('about/',viewAbout,name='about'), 
    path('service/',viewService,name="service"),
    
]
