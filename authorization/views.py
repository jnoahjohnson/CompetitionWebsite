from django.shortcuts import render
from django.http import HttpResponse

def LoginPageView(request) :
    return render(request, 'authorization/login.html') 

def LogoutPageView(request) :
    return render(request, 'authorization/login.html')

def ProfilePageView(request) :
    return render(request, 'authorization/profile.html') 