from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
from .models import BMImodel
from .forms import BMIform
from .serializer import BMIserializer
from .utils2 import *
from django.contrib.auth import login,logout,authenticate
import datetime
from django.contrib.auth.models import User


# Create your views here.
def create(request):
    if request.method == 'POST':
        form = BMIform(request.POST)
        if form.is_valid():
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            current_dt = datetime.date.today()
            bmi = round(weight / (height ** 2),3)
            instance = form.save(commit=False)
            instance.bmi = bmi
            instance.save()
            #print(request.user.username)
            msg=send_BMI_email(request.user.username,bmi,current_dt)
            
            messages.success(request, msg)
            return redirect('home')
            
    form = BMIform()
    return render(request, 'create.html', {'fm': form})
                
    
	
def home(request):
    data=BMImodel.objects.all()
    return render(request,"home.html",{"data":data})


def remove(request,k):
    del_id=BMImodel.objects.get(id=k)
    del_id.delete()
    return redirect("home")

def ulogout(request):
	logout(request)
	return redirect("ulogin")


def update(request, k):
    instance = get_object_or_404(BMImodel, id=k)
    form = BMIform(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    
    context = {
        'form': form,
        'instance': instance
    }
    
    return render(request, 'update.html', context)
	

def cp(request):
	
	if request.method=="POST":
		
		pw1=request.POST.get("pw1")
		pw2=request.POST.get("pw2")
		if pw1==pw2:
			try:
				usr=User.objects.get(username=request.user.username)
				usr.set_password(pw1)
				usr.save()
				return redirect("home")
			except User.DoesNotExist:
				return redirect(request,"cp.html",{"msg":"user does not exists"})
		else:
			return render(request,"cp.html",{"msg":"passwords did not match"})
	else:
		return render(request,"cp.html")
			

#CRUD with API

@api_view(["GET","DELETE"])
def eo(request,i=None):
	if request.method=="GET":
		result=BMImodel.objects.all()
		ser_result=BMIserializer(result,many=True)
		return Response(ser_result.data)
	elif request.method=="DELETE":	
		try:	
			emp=BMImodel.objects.get(id=i)   #modelfield=requestinputfield
			emp.delete()
			return Response({"msg":"emp deleted"})
		except BMImodel.DoesNotExist:
			return Response({"msg":"BMI does not exists"}) 
