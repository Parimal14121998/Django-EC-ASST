from django.contrib import admin
from django.urls import path
from EC_App1.views import ulogin,usignup,ulogout,verify

urlpatterns = [
    
    path('ulogin',ulogin,name='ulogin'),
    path('usignup',usignup,name='usignup'),
    path('ulogout',ulogout,name='ulogout'),
    path('verify/<str:token>/',verify),
]

