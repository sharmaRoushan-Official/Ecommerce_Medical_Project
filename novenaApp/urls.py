from django.urls import path
from .views import *


urlpatterns = [
    path('home/',viewHome), # http://127.0.0.1:8000/novapp/home/
    
]
