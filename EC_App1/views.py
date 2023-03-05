from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .utils import *
from .models import *
import uuid
from EC_crud import urls2


def ulogin(request):
	if request.user.is_authenticated:
		return redirect("home")
	elif request.method=="POST":
		un=request.POST.get("un")
		pw=request.POST.get("pw")
		usr=authenticate(username=un,password=pw)
		if usr is not None:
			login(request,usr)
			return redirect("home")
		else:	
			return render(request,"login.html",{"msg":"invalid username and password"})
	else:
		return render(request,"login.html")


def usignup(request):
	if request.user.is_authenticated:
		return redirect("home")
	elif request.method=="POST":
		un=request.POST.get("un")
		pw1=request.POST.get("pw1")

		try:
			usr=User.objects.get(username=un)
			return render(request,"signup.html",{"msg":"user already exists"})
		except User.DoesNotExist:
			usr=User.objects.create_user(username=un,password=pw1)
			usr.save()
			p_obj= Profile.objects.create(user=usr,email_token=str(uuid.uuid4()))
			p_obj.save()
			send_token_email(usr,p_obj.email_token)
			return HttpResponse("Plz chk your email to verify")

			
	else:
		return render(request,"signup.html")
	
def verify(request,token):
	try:
		
		t_obj=Profile.objects.get(email_token = token)
		t_obj.is_verified = True
		t_obj.save()
		return redirect(ulogin)
	except Exception as e:
		return render(request,"signup.html",{"msg":"Invalid Token"})
	
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
			

def ulogout(request):
	logout(request)
	return redirect("ulogin")

