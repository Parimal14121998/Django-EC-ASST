
from django.contrib import admin
from django.urls import path
from EC_crud.views import home,create,remove,ulogout,update,cp,eo

urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('remove/<int:k>',remove,name='remove'),
    path('ulogout',ulogout,name='ulogout'),
    path('update/<int:k>',update,name='update'),
    path('cp',cp,name='cp'),
    path('eo/',eo),
    path('eo/<int:i>',eo),
]

