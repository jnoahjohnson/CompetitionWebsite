from django.http import HttpResponse
from django.shortcuts import render



def indexPageView(request):
    return render(request, 'competitions/index.html')


def createCompetitions(request):
    return HttpResponse('Create Competition')


def editCompetitions(request):
    return HttpResponse('Edit Competitions')


def viewCompetitions(request):
    return HttpResponse('View Competition')
