from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Authorization Index') 

def Login(request) :
    return HttpResponse('Login Authorization') 

def Logout(request) :
    return HttpResponse('Logout Authorization') 