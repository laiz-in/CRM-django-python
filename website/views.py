import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from website.EmailBackEnd import EmailBackEnd

def home(request):
    if request.user.is_authenticated:
            # Redirect based on user type
            if request.user.user_type == "1":
                # User type 1, redirect to a specific view
                return HttpResponseRedirect(reverse("admin_home"))
            elif request.user.user_type == "2":
                # User type 2, redirect to a specific view
                return HttpResponseRedirect(reverse("staff_home"))
            elif request.user.user_type == "3":
                # User type 3, redirect to a specific view
                return HttpResponseRedirect(reverse("student_home"))
            # Add more conditions for additional user types if needed
    else:
        # User is not authenticated, render the home template
        return render(request, "home.html")
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not beacause it says , its not post</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"Invalid login details. please try again!")
            return HttpResponseRedirect(reverse("home"))


def GetUserDetails(request):
    if request.user!=None:
         return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
         return HttpResponse("Please Login First")

def logout_user(request):
    logout(request)
    messages.error(request,"you have logged out !")
    return HttpResponseRedirect("home")