from django.shortcuts import render
from django.http import HttpResponse

def LoginPageView(request) :
    return render(request, 'authorization/index.html') 

def LogoutPageView(request) :
    return HttpResponse('Logout Authorization') 

def ProfilePageView(request) :
    return HttpResponse('Profile Page') 